"""Write search_log_cn.md: fixed narrative header (scripts/search_log_header_cn.md) + per-group statistics
computed from seeds/queries, cache/candidates, seeds/papers and state.

  python3 -I scripts/build_searchlog_en.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CACHE, CATS, ROOT, SCRIPTS, SEEDS, load, window_status  # noqa: E402
import papers_en  # noqa: E402


def main():
    out = [(SCRIPTS / "search_log_header_cn.md").read_text().rstrip(), "",
           "## 各课程群检索统计（由脚本生成）", "",
           "| 群 | 检索式条数 | 候选（去重 arXiv ID） | 候选中近三年 | 种子（主列表/后备） | 已核验 | 待核验 | 失败 | 跨群让出/修订移出 |",
           "|---|---|---|---|---|---|---|---|---|"]
    for g in CATS:
        qs = load(SEEDS / "queries" / f"{g}_en.json", [])
        cands = load(CACHE / "candidates" / f"{g}_en.json", {})
        recent = 0
        for aid in cands:
            m = load(papers_en.meta_file(aid), None)
            recent += bool(m) and window_status(m["v1_date"]) == "近三年"
        ss = papers_en.seeds(g)
        st = load(papers_en.state_path(g), {})
        cnt = {k: sum(1 for v in st.values() if v["status"] == k) for k in ("ok", "pending", "fail")}
        moved = sum(1 for v in st.values() if v["status"] in ("dup_elsewhere", "superseded"))
        main_n = sum(1 for s in ss if not s.get("reserve"))
        out.append(f"| {g} {CATS[g][1]} | {len(qs)} | {len(cands)} | {recent} | {main_n}/{len(ss) - main_n} | "
                   f"{cnt['ok']} | {cnt['pending']} | {cnt['fail']} | {moved} |")
    out += ["", "## 检索式全文", "", "各群检索式见 `scripts/seeds/queries/NN_en.json`（字段 q 为 arXiv search_query，"
            "subtopic 为子主题；未标 old 的检索式自动附加日期窗口 submittedDate:[20231029 TO 20261029]）。示例（每群前 3 条）：", ""]
    for g in CATS:
        qs = load(SEEDS / "queries" / f"{g}_en.json", [])
        out.append(f"- **{g} {CATS[g][1]}**：" + "；".join(f"`{q['q'][:90]}`（{q.get('subtopic', '')}）" for q in qs[:3]))
    gaps = sorted((SCRIPTS / "annotations").glob("*gap*_cn.md"))
    if gaps:
        out += ["", "## 缺口说明文件", ""] + [f"- `scripts/annotations/{p.name}`" for p in gaps]
    (ROOT / "search_log_cn.md").write_text("\n".join(out) + "\n")
    print("search_log_cn.md written")


if __name__ == "__main__":
    main()
