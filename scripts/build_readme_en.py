"""Write README_cn.md from the current catalog/progress files (run after build_catalog_en.py).

  python3 -I scripts/build_readme_en.py
"""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CATS, ROOT, STATE  # noqa: E402


def rows(name):
    p = ROOT / name
    return list(csv.DictReader(open(p, encoding="utf-8-sig"))) if p.exists() else []


def main():
    cat, prog, fails = rows("catalog_cn.csv"), rows("progress_cn.csv"), rows("download_failures_cn.csv")
    s = json.loads((STATE / "summary_en.json").read_text())
    reuse = [r for r in cat if r["来源性质"].startswith("已有复用")]
    papers = [r for r in cat if r["资料编号"].startswith("P")]
    recent = sum(r["时间窗口"] == "近三年" for r in papers)
    by_type = Counter(r["资料类型"] for r in papers)
    courses = [r for r in cat if r["资料编号"].startswith("A") and "不单独计数" not in r["资料类型"]]
    supp = [r for r in cat if "不单独计数" in r["资料类型"]]
    fail_kind = Counter(r["状态"].split("：")[0] for r in fails)
    L = []
    L += ["# 人工智能本科—研究生课程资料库（ai_undergraduate_graduate_curriculum_literature）", "",
          "按课程群组织、可按顺序学习的 AI 资料库：官方课程讲义（A）、教科书与参考书（B）、论文/综述/学术教程（C，编号 P）、"
          "官方实践材料（D），以及官方培养方案参考（C-xx）。检索日 2026-10-29。**只有完整下载并核验通过的资料才计数。**", "",
          "## 一、总量（由脚本按当前状态生成）", "",
          "| 类别 | 已核验数量 |", "|---|---|",
          f"| 培养方案参考（不计入教材/课程） | {s['curricula']} |",
          f"| 课程（完整讲义/完整课件包/OCW 官方包） | {len(courses)}（另有 {len(supp)} 条补充课件并入所属课程，不单独计数） |",
          f"| 教科书/参考书 | {s['books']} |",
          f"| 论文、综述与学术教程 | {s['papers']}（近三年 {recent}，占 {recent / max(1, len(papers)):.1%}；三年前经典 {len(papers) - recent}） |",
          f"| 官方实践材料 | {s['practice']} |",
          f"| 全库去重条目（catalog 行数） | {len(cat)} |",
          f"| 其中新下载 / 已有复用 | {len(cat) - len(reuse)} / {len(reuse)} |",
          f"| 失败、残缺、排除与待核验记录 | {len(fails)}（{'；'.join(f'{k} {v}' for k, v in fail_kind.items())}） |", "",
          "论文类型分布：" + "；".join(f"{k} {v}" for k, v in by_type.most_common()), "",
          "## 二、各课程群进度", "",
          "| 课程群 | 层次 | 课程 | 教材 | 论文（近三年占比） | 三年前经典 | 实践 | 状态 |", "|---|---|---|---|---|---|---|---|"]
    for p in prog:
        L.append(f"| {p['课程群']} | {p['层次']} | {p['课程（核验通过）']} | {p['教科书/参考书']} | {p['论文等已核验全文']}（{p['近三年占比']}） | "
                 f"{p['三年前经典篇数']} | {p['官方实践材料']} | {p['状态句']} |")
    L += ["", "## 三、目录结构", "",
          "```",
          "ai_undergraduate_graduate_curriculum_literature/",
          "├── README_cn.md              本文件",
          "├── catalog_cn.csv            全库元数据（每条已核验资料一行，37 列）",
          "├── progress_cn.csv           各课程群进度与近三年占比",
          "├── search_log_cn.md          检索来源、检索式、受限来源、筛选规则",
          "├── download_failures_cn.csv  失败、残缺、排除、待核验记录（不计数）",
          "├── curricula/                官方培养方案与课程目录（C-xx，仅作参考）",
          "├── courses/                  课程讲义/课件包/OCW 官方整包（A）",
          "├── books/                    教科书与参考书（B；PDF 或 *_html_<lang>/ 离线 HTML）",
          "├── papers/NN_<slug>/         论文、综述、学术教程（P），按课程群分目录",
          "├── practice/                 官方实践材料（D；仓库快照目录含 SNAPSHOT_<lang>.txt 记录提交号）",
          "├── guides/                   学习指南（课程体系图、本科/研究生/工程路线、核心阅读清单、实践项目）",
          "└── scripts/                  全部脚本、种子清单、检索式、状态与缓存",
          "```", "",
          "命名：所有自行创建和下载的文件在扩展名前标注语言（`_en` 英文、`_cn` 中文、`_cn_en` 双语）；"
          "HTML 离线包与仓库快照为目录，目录名带语言后缀，目录内保留官方原文件名以保证链接可用。", "",
          "## 四、计数与核验规则", "",
          "- 论文：HTTP 200（或兄弟库已核验文件复制后重新核验）、%PDF 头、pypdf 可解析、≥4 页、≥12000 字符、前两页标题词匹配 ≥0.8、"
          "第一作者姓氏可见、有参考文献节；只差标题/作者检查的列为待核验，不计数。首次公开日按 arXiv v1 记，修订版本与日期另记。",
          "- 教材：作者/出版社官方全文，书名短语出现在前 12 页、页数达到下限；按章节开放的书下载目录列出的全部章节，整本计一次；"
          "官方 HTML 教材按目录保存全部页面（离线包，单列格式）。",
          "- 课程：完整讲义包或完整课件包计一次；缺讲次的不计（如 CMU 10-708 笔记缺 1 讲，列入失败清单）；只有幻灯片的标为“完整课件包”。",
          "- 实践：官方仓库按提交号快照或官方页面；记录学习目标、环境与许可证；未执行任何项目，未下载数据集与模型权重。",
          "- 培养方案：仅作“培养方案参考”，不计为教材或课程。",
          "- 跨群：同一论文只计入编号最小的课程群；同一书不同版本、同一课程不同学期不重复收录。",
          "- 简介依据：论文为 arXiv 摘要，教材/课程为官方简介与目录；未声称读过全文。",
          "- 按用户此前要求，未另做整库 SHA256 扫描；catalog 中的 SHA256 是下载时顺带计算的单文件值。", "",
          "## 五、续跑方式", "",
          "所有命令在库根目录运行（Python 一律 `python3 -I`）：",
          "```bash",
          "# 论文：逐群下载核验，已完成条目自动跳过；失败条目重试加 --retry-failed",
          "for g in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20; do python3 -I -u scripts/papers_en.py download $g; done",
          "python3 -I scripts/papers_en.py status            # 各群进度句",
          "python3 -I scripts/papers_en.py text <KEY>         # 查看待核验条目首页文字；manual/reject 人工处理",
          "# 教材/课程/实践/培养方案",
          "python3 -I scripts/materials_en.py fetch books --retry-failed      # 或 courses / practice / curricula",
          "python3 -I scripts/materials_en.py status",
          "# 重建目录、进度、失败清单、检索日志与本 README",
          "python3 -I scripts/build_catalog_en.py && python3 -I scripts/build_searchlog_en.py && python3 -I scripts/build_readme_en.py",
          "```",
          "注意：arXiv 限速锁与本机其他文献库共用（`/root/.cache/ipm_lit/locks/arxiv.org`，每 5 秒 1 次）；同一课程群不要同时运行两个 download。"
          "工作目录（暂存、被替换文件）在 `/root/.cache/aiug_lit/`，不在库内。", "",
          "## 六、学习指南", "",
          "- `guides/curriculum_map_cn.md` 课程体系、各校方案对照、层次与先修",
          "- `guides/undergraduate_path_cn.md` 本科路线",
          "- `guides/graduate_path_cn.md` 研究生路线",
          "- `guides/engineering_path_cn.md` 工程实践路线",
          "- `guides/core_reading_list_cn.md` 核心阅读清单（章节已核对目录）",
          "- `guides/practice_projects_cn.md` 配套实践项目（只整理，未执行）"]
    (ROOT / "README_cn.md").write_text("\n".join(L) + "\n")
    print("README_cn.md written")


if __name__ == "__main__":
    main()
