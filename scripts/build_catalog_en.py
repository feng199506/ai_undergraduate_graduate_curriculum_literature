"""Build catalog_cn.csv, progress_cn.csv and download_failures_cn.csv from seeds + state.

  python3 -I scripts/build_catalog_en.py

Only verified items get a 资料编号 and count. IDs: A<group>-NN courses, B<group>-NN books,
C-NN curriculum references, D<group>-NN practice, P<group>-NNN papers (numbered in reading order
among verified papers). Failed / excluded / pending items go to download_failures_cn.csv.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CATS, ROOT, SEEDS, STATE, load, window_status  # noqa: E402
import papers_en  # noqa: E402
import materials_en  # noqa: E402

COLS = ["资料编号", "课程群", "交叉课程群", "子主题", "学位层次", "必修/选修", "资料类型", "资料形式", "标题", "作者或教师",
        "学校或出版社", "课程代码", "学期或版本", "原著/首次公开日期", "首次公开日期依据", "版本或修订日期", "时间窗口",
        "三年前保留理由", "标识符", "语言", "原始来源", "下载链接", "本地路径", "来源性质", "下载及完整性状态", "核验说明",
        "SHA256", "页数/文件数", "许可证", "先修要求", "难度", "选入理由", "简介", "简介依据", "学习目标", "环境要求",
        "阅读顺序"]
LANG = {"en": "英文", "cn": "中文", "cn_en": "中英双语"}


def first_file(r):
    return (r.get("files") or [{}])[0]


def material_rows(kind, set_name, prefix_fn):
    rows, fails, counters = [], [], defaultdict(Counter)
    order = defaultdict(int)
    for it in materials_en.manifest(set_name):
        st = load(materials_en.res_path(it["mid"]), {})
        g = it.get("group", "00")
        if st.get("status") != "verified" or it.get("exclude") or it.get("incomplete"):
            why = it.get("exclude_reason") or it.get("incomplete") or st.get("note") or "尚未下载"
            fails.append({"条目": it["mid"], "课程群": g, "类别": kind, "标题": it["title"],
                          "来源": it.get("url") or it.get("index_url") or it.get("repo") or (it.get("urls") or [""])[0],
                          "状态": ("残缺（文件保留，不计数）：" + first_file(st).get("path", "") if it.get("incomplete")
                                   else "排除" if it.get("exclude") else ("下载/核验失败" if st else "待下载")), "原因": why})
            continue
        order[g] += 1
        f = first_file(st)
        files = st.get("files", [])
        size = (f"{sum(x.get('pages', 0) for x in files)} 页 / {len(files)} 个文件" if any("pages" in x for x in files)
                else f"{f.get('html_pages', f.get('files', ''))} 页面/文件")
        reuse = "已有复用（{} {}）".format(it.get("src_lib", ""), it.get("src_id", "")) if st.get("reuse") else "新下载"
        pack = it.get("pack_type", "")
        form = {"pdf": "PDF", "pdfs": "多 PDF 资料包", "zip": "官方压缩包", "html": "官方 HTML 离线包",
                "git": "官方仓库快照", "reuse": "PDF/目录（复用）"}[it["kind"]]
        oy = it.get("orig_year") or it.get("term") or it.get("academic_year", "")
        rows.append({
            "资料编号": prefix_fn(it, order[g]), "课程群": f"{g} {CATS[g][1]}" if g in CATS else "培养方案参考",
            "交叉课程群": "、".join(it.get("related", [])), "子主题": it.get("subtopic", ""),
            "学位层次": it.get("level") or it.get("degree", ""), "必修/选修": it.get("requirement") or (CATS[g][3] if g in CATS else ""),
            "资料类型": kind + (f"（{pack}）" if pack else ""), "资料形式": form, "标题": it["title"],
            "作者或教师": it.get("authors") or it.get("instructors", ""), "学校或出版社": it.get("institution", ""),
            "课程代码": it.get("code", "") or it.get("program", ""), "学期或版本": it.get("term") or it.get("edition") or it.get("academic_year", ""),
            "原著/首次公开日期": str(oy), "首次公开日期依据": "原著出版年/课程学期/方案学年（教材与课程不套用论文年份比例）",
            "版本或修订日期": str(it.get("edition_year", "")), "时间窗口": "教材/课程/方案（不适用）", "三年前保留理由": "",
            "标识符": it.get("code", "") or st.get("commit", ""), "语言": LANG.get(it.get("lang", "en"), it.get("lang", "")),
            "原始来源": it.get("syllabus_url") or it.get("source_page") or it.get("index_url") or it.get("repo") or it.get("url", ""),
            "下载链接": f.get("url", "") or it.get("url", ""), "本地路径": f.get("path", ""), "来源性质": reuse,
            "下载及完整性状态": "已下载，完整性核验通过", "核验说明": st.get("note", ""), "SHA256": f.get("sha256", "") or f.get("archive_sha256", ""),
            "页数/文件数": size, "许可证": it.get("license", ""), "先修要求": it.get("prereq", ""), "难度": it.get("difficulty", ""),
            "选入理由": it.get("reason", ""), "简介": it.get("summary", "") or it.get("syllabus_note", ""),
            "简介依据": it.get("summary_basis", "官方页面"), "学习目标": it.get("learning_goals", ""), "环境要求": it.get("environment", ""),
            "阅读顺序": order[g]})
        if it.get("supplement_of"):
            rows[-1]["资料类型"] = f"课程补充课件（并入 {it['supplement_of']}，不单独计数）"
        else:
            counters[g][kind + (f"（{pack}）" if pack else "")] += 1
    return rows, fails, counters


def paper_rows():
    rows, fails, stats = [], [], {}
    for g in CATS:
        st = load(papers_en.state_path(g), {})
        n = 0
        recent = old = reuse = 0
        for s in papers_en.seeds(g):
            k = papers_en.key_of(s)
            rec = st.get(k)
            m = papers_en.entry_meta(s) if rec else None
            if not rec or rec["status"] != "ok":
                if rec and rec["status"] in ("fail", "pending", "rejected"):
                    fails.append({"条目": k, "课程群": g, "类别": "论文", "标题": (m or {}).get("title", s.get("title", "")),
                                  "来源": rec.get("pdf", ""), "状态": {"fail": "下载/核验失败", "pending": "待人工核验",
                                                                     "rejected": "人工拒收"}[rec["status"]], "原因": rec.get("note", "")})
                continue
            n += 1
            w = window_status(m["date"])
            recent += w == "近三年"
            old += w == "三年前"
            reuse += rec.get("source") == "reuse"
            ref = " ".join(x for x in (m.get("journal_ref"), m.get("comment")) if x)
            rows.append({
                "资料编号": f"P{g}-{n:03d}", "课程群": f"{g} {CATS[g][1]}", "交叉课程群": "、".join(s.get("related", [])),
                "子主题": s.get("subtopic", ""), "学位层次": s.get("level", ""), "必修/选修": CATS[g][3],
                "资料类型": s.get("type", ""), "资料形式": "PDF", "标题": m["title"], "作者或教师": "; ".join(m["authors"][:8]) + (" 等" if len(m["authors"]) > 8 else ""),
                "学校或出版社": ref[:200] if ref else "arXiv 预印本（未核实正式发表）", "课程代码": "", "学期或版本": m["version"],
                "原著/首次公开日期": m["date"], "首次公开日期依据": m["date_basis"], "版本或修订日期": m["version_date"], "时间窗口": w,
                "三年前保留理由": s.get("classic_reason", ""), "标识符": (f"arXiv:{s['arxiv']}" if s.get("arxiv") else "") + (f"; DOI:{m['doi']}" if m.get("doi") else ""),
                "语言": "中文" if Path(rec["path"]).stem.endswith("_cn") else "英文", "原始来源": m["landing"], "下载链接": rec.get("pdf", ""),
                "本地路径": rec["path"], "来源性质": f"已有复用（{rec.get('reuse_lib')} {rec.get('reuse_id')}）" if rec.get("source") == "reuse" else "新下载",
                "下载及完整性状态": "已下载，全文核验通过", "核验说明": rec.get("note", ""), "SHA256": rec.get("sha256", ""),
                "页数/文件数": f"{rec.get('pages', '')} 页", "许可证": "", "先修要求": "", "难度": s.get("difficulty", ""),
                "选入理由": s.get("reason", ""), "简介": s.get("summary", ""), "简介依据": s.get("summary_basis", "arXiv 摘要；未读全文"),
                "学习目标": "", "环境要求": "", "阅读顺序": n})
        stats[g] = {"ok": n, "recent": recent, "old": old, "reuse": reuse,
                    "pending": sum(1 for v in st.values() if v["status"] == "pending"),
                    "fail": sum(1 for v in st.values() if v["status"] == "fail")}
    return rows, fails, stats


def main():
    B, fb, cb = material_rows("教科书/参考书", "books", lambda it, n: it["mid"])
    A, fa, ca = material_rows("课程", "courses", lambda it, n: it["mid"])
    D, fd, cd = material_rows("官方实践材料", "practice", lambda it, n: it["mid"])
    C, fc, cc = material_rows("培养方案参考", "curricula", lambda it, n: it["mid"])
    P, fp, ps = paper_rows()
    rows = C + A + B + P + D
    with open(ROOT / "catalog_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, COLS)
        w.writeheader()
        w.writerows(rows)
    fcols = ["条目", "课程群", "类别", "标题", "来源", "状态", "原因"]
    with open(ROOT / "download_failures_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fcols)
        w.writeheader()
        w.writerows(fc + fa + fb + fp + fd)
    pcols = ["课程群", "层次", "课程（核验通过）", "其中完整文字讲义", "其中完整课件包", "其中讲义+课件", "其中OCW官方课程包",
             "教科书/参考书", "论文等已核验全文", "论文目标", "近三年篇数", "三年前经典篇数", "近三年占比", "已有复用论文", "待核验",
             "论文下载失败", "官方实践材料", "状态句"]
    prog = []
    for g in CATS:
        cnt = ca.get(g, Counter())
        ncourse = sum(cnt.values())
        p = ps[g]
        ratio = f"{p['recent'] / p['ok']:.1%}" if p["ok"] else ""
        prog.append({"课程群": f"{g} {CATS[g][1]}", "层次": f"{CATS[g][2]}；{CATS[g][3]}", "课程（核验通过）": ncourse,
                     "其中完整文字讲义": sum(v for k, v in cnt.items() if "完整文字讲义" in k),
                     "其中完整课件包": sum(v for k, v in cnt.items() if "完整课件包" in k),
                     "其中讲义+课件": sum(v for k, v in cnt.items() if "讲义+课件" in k),
                     "其中OCW官方课程包": sum(v for k, v in cnt.items() if "OCW" in k),
                     "教科书/参考书": sum(cb.get(g, Counter()).values()), "论文等已核验全文": p["ok"], "论文目标": 50,
                     "近三年篇数": p["recent"], "三年前经典篇数": p["old"], "近三年占比": ratio, "已有复用论文": p["reuse"],
                     "待核验": p["pending"], "论文下载失败": p["fail"], "官方实践材料": sum(cd.get(g, Counter()).values()),
                     "状态句": f"已核验完整资料 {p['ok']} / 目标约 50；待核验 {p['pending']}；下载失败 {p['fail']}。"})
    with open(ROOT / "progress_cn.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, pcols)
        w.writeheader()
        w.writerows(prog)
    tot_p = sum(p["ok"] for p in ps.values())
    tot_r = sum(p["recent"] for p in ps.values())
    summary = {"curricula": len(C), "courses": len(A), "books": len(B), "papers": tot_p, "practice": len(D),
               "papers_recent": tot_r, "papers_old": sum(p["old"] for p in ps.values()),
               "reuse": sum(1 for r in rows if r["来源性质"].startswith("已有复用")),
               "failures": len(fc + fa + fb + fp + fd), "total_unique": len(rows)}
    (STATE / "summary_en.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
