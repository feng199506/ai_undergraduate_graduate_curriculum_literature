"""Shared helpers for the AI undergraduate-to-graduate curriculum library (AIUG).

Paths, per-host rate limiting (cross-process flock), bounded-retry HTTP GET,
text normalisation, the three-year window and atomic JSON load/save.

Rate limits: arXiv >= 5 s between requests (API and PDF share one budget; the lock file is
shared with the industrial-process-monitoring library so the two never stack on arXiv),
Crossref >= 1.5 s, every other host >= 2 s. 4xx other than 429 is never retried.
"""
import fcntl
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
CACHE = SCRIPTS / "cache"
STATE = SCRIPTS / "state"
SEEDS = SCRIPTS / "seeds"
ANNOT = SCRIPTS / "annotations"
WORK = Path(os.environ.get("AIUG_WORK", "/root/.cache/aiug_lit"))   # on disk, outside the library
STAGING = WORK / "staging"
PYLIB = WORK / "pylib"
LOCK_DIR = WORK / "locks"
SHARED_LOCKS = {"arxiv.org": Path("/root/.cache/ipm_lit/locks/arxiv.org")}
UA = "Mozilla/5.0 (compatible; aiug_curriculum_literature/1.0; personal study library, low request rate)"

SEARCH_DATE = "2026-10-29"
WINDOW_START, WINDOW_END = "2023-10-29", "2026-10-29"

# id: (slug, Chinese name, level tags, requirement tag)
CATS = {
    "01": ("math_foundations", "数学基础", "本科基础", "必修基础"),
    "02": ("probability_statistics", "概率与统计", "本科基础", "必修基础"),
    "03": ("optimization_information_theory", "优化与信息论", "本科进阶/研究生核心", "必修基础"),
    "04": ("cs_programming_foundations", "计算机科学与编程基础", "本科基础", "必修基础"),
    "05": ("ai_foundations", "人工智能基础", "本科进阶", "必修基础"),
    "06": ("machine_learning", "机器学习", "本科进阶/研究生核心", "必修基础"),
    "07": ("deep_learning", "深度学习", "本科进阶/研究生核心", "必修基础"),
    "08": ("probabilistic_graphical_models", "概率图模型与概率机器学习", "研究生核心", "选修方向"),
    "09": ("natural_language_processing", "自然语言处理", "本科进阶/研究生核心", "选修方向"),
    "10": ("llm_agents", "大语言模型与智能体", "研究生专题", "选修方向"),
    "11": ("computer_vision", "计算机视觉", "本科进阶/研究生核心", "选修方向"),
    "12": ("generative_multimodal", "生成模型与多模态学习", "研究生专题", "选修方向"),
    "13": ("reinforcement_learning_control", "强化学习与控制", "研究生核心", "选修方向"),
    "14": ("robotics_embodied_ai", "机器人与具身智能", "研究生专题", "选修方向"),
    "15": ("time_series_signal_processing", "时间序列与信号处理", "本科进阶/研究生专题", "选修方向"),
    "16": ("graph_learning_recommender", "图学习与推荐系统", "研究生专题", "选修方向"),
    "17": ("causal_inference_sciml", "因果推断与科学机器学习", "研究生专题", "选修方向"),
    "18": ("trustworthy_ai", "可信人工智能", "研究生核心/研究生专题", "选修方向（部分项目必修伦理）"),
    "19": ("ai_systems_deployment", "人工智能系统与部署", "研究生专题", "选修方向（工程侧重）"),
    "20": ("research_methods_practice", "研究方法与综合实践", "贯穿本科高年级至研究生", "必修基础（毕业设计/论文）"),
}

INTERVAL = {"arxiv.org": 5.0, "api.crossref.org": 1.5}

STOP = {"a", "an", "the", "of", "for", "and", "in", "on", "with", "to", "via", "by", "is", "are",
        "from", "at", "as", "its", "do", "how", "can", "using", "based", "towards", "toward", "under"}


def cat_dir(cat):
    return f"{cat}_{CATS[cat][0]}"


def cat_label(cat):
    return f"{cat} {CATS[cat][1]}"


def host_key(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    return "arxiv.org" if host.endswith("arxiv.org") else host


def wait(key, interval):
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    path = SHARED_LOCKS.get(key) or LOCK_DIR / re.sub(r"[^A-Za-z0-9._-]", "_", key)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        raw = f.read().strip()
        try:
            last = float(raw) if raw else 0.0
        except ValueError:
            last = 0.0
        delay = interval - (time.time() - last)
        if delay > 0:
            time.sleep(delay)
        f.seek(0)
        f.truncate()
        f.write(str(time.time()))


def http(url, accept="*/*", timeout=120, tries=3, headers=None, max_bytes=600_000_000):
    """Return (status, body_bytes, final_url, content_type)."""
    key = host_key(url)
    err = ""
    for attempt in range(tries):
        wait(key, INTERVAL.get(key, 2.0))
        try:
            h = {"User-Agent": UA, "Accept": accept, **(headers or {})}
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(max_bytes), r.geturl(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
            if e.code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            if 400 <= e.code < 500:
                return e.code, b"", url, ""
        except Exception as e:  # network error / timeout
            err = repr(e)[:200]
        time.sleep(6 * (attempt + 1))
    return None, err.encode(), url, ""


def get_json(url, **kw):
    st, body, _, _ = http(url, accept="application/json", **kw)
    if st != 200:
        return None
    try:
        return json.loads(body)
    except ValueError:
        return None


def fold(s):
    s = re.sub(r"[{}\\$]", "", s or "")
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "")


def norm(s):
    """Title key for dedup: lower-case ASCII alnum, CJK kept."""
    s = unicodedata.normalize("NFKC", strip_tags(s or "")).lower()
    return "".join(ch for ch in s if ch.isalnum())


def has_cjk(s):
    return any("一" <= ch <= "鿿" for ch in s or "")


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", fold(strip_tags(s)).lower()) if t not in STOP and len(t) > 1]


def title_similarity(a, b):
    if has_cjk(a) or has_cjk(b):
        ca, cb = set(norm(a)), set(norm(b))
        return len(ca & cb) / max(1, len(ca | cb))
    ta, tb = set(tokens(a)), set(tokens(b))
    return len(ta & tb) / max(1, len(ta | tb))


def title_in_text(title, text):
    """Fraction of title tokens (or CJK characters) present in text, whitespace-insensitive."""
    if has_cjk(title):
        tt = [c for c in norm(title) if "一" <= c <= "鿿"]
        blob = norm(text)
        return sum(1 for c in tt if c in blob) / len(tt) if tt else 0.0
    tt = tokens(title)
    blob = re.sub(r"[^a-z0-9]", "", fold(text).lower())
    return sum(1 for t in tt if t in blob) / len(tt) if tt else 0.0


def surname(name):
    name = (name or "").strip()
    if has_cjk(name):
        return name[:1]
    if "," in name:
        name = name.split(",")[0]
    parts = fold(name).split()
    return re.sub(r"[^A-Za-z]", "", parts[-1]) if parts else "Anon"


def short_title(title, n=4):
    title = fold(strip_tags(title))
    head = title.split(":")[0].strip()
    if ":" in title and 1 <= len(head.split()) <= 3:
        words = re.findall(r"[A-Za-z0-9]+", head)
    else:
        words = [w for w in re.findall(r"[A-Za-z0-9]+", title) if w.lower() not in STOP][:n]
    return "".join(w[:1].upper() + w[1:] for w in words)[:40] or "Untitled"


def window_status(date):
    """date is YYYY, YYYY-MM or YYYY-MM-DD."""
    if not date:
        return "待核实"
    lo = (date + "-01-01")[:10]
    hi = (date + "-12-31")[:10] if len(date) == 4 else (date + "-31")[:10]
    if lo >= WINDOW_START and hi <= WINDOW_END:
        return "近三年"
    if hi < WINDOW_START:
        return "三年前"
    return "待核实（日期精度不足）"


def load(path, default):
    path = Path(path)
    return json.loads(path.read_text()) if path.exists() else default


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1))
    os.replace(tmp, path)
