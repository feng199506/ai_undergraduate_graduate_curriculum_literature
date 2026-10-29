# 课程（A 类）与实践材料（D 类）规范

库根目录 LIB=`/root/ai_undergraduate_graduate_curriculum_literature`。命令在 LIB 下运行，Python 一律 `python3 -I`。
下载核验脚本：`scripts/materials_en.py`（先读它的文档字符串，了解 kind：pdf / pdfs / zip / html / reuse / git）。
检索日 2026-10-29。不绕过付费墙、登录、表单或访问限制；不下载课程视频、模型权重、数据集。

## A. 官方课程与完整讲义（每群 3–5 套互补课程）
- 优先著名大学官方公开材料（课程官网、MIT OCW、教师主页、官方 GitHub）。优先近期学期；经典课程可保留，记录学期。
- **只计完整资料**：完整文字讲义（全部讲次 notes）或完整课件包（全部讲次 slides）或 OCW 官方整门课程压缩包。缺讲次、只有大纲、只有视频链接、只有阅读清单的不计。
  - 用 `pdfs` + `index_url` + `link_regex` 从官方课程日程页抓取全部讲次 PDF；`min_files` 设为日程页实际讲次数（先人工看页面确认讲次数），防止漏抓。
  - 只有幻灯片的课程，`pack_type` 写 `完整课件包`；有完整文字讲义写 `完整文字讲义`；两者都有写 `讲义+课件`；OCW 整包写 `OCW 官方课程包`。
  - 课程网页是 HTML 讲义（如 CS231n notes）用 `html`，`link_regex` 限定讲义页。
- 兄弟库已核验过的课程可复用（`kind: "reuse"`，`src` 填源路径，`src_lib`、`src_id` 填源库名与编号）。可复用清单见 `scripts/annotations/reusable_materials_cn.md`。
- 同一课程不同学期只收一个。

## D. 官方实践材料（每群 2–5 套）
- 公开作业、实验说明、教程、参考项目：官方课程作业仓库、官方教程仓库（如 d2l、Hugging Face 课程、PyTorch 教程、Spinning Up、CS336 作业等）。
- 用 `git`（官方仓库，记录 commit）或 `pdfs`/`html`/`zip`。仓库归档设 `max_mb`（默认 400）；过大的（含数据/权重）不要收，换别的。
- 记录：`learning_goals`（学习目标）、`environment`（语言/框架/硬件要求，依据仓库 README 或说明页）、`license`（依据仓库 LICENSE 或页面声明；没有就写"未声明许可证"）。
- 不执行项目，只下载保存。

## 清单文件与字段
你写自己的分片文件（不要改别人的）：`scripts/seeds/materials/courses_<分片>_cn.json`、`scripts/seeds/materials/practice_<分片>_cn.json`（分片名由主会话指定）。JSON 列表，每条：
- 公共：`mid`（课程 `A<群号>-<两位序号>`，如 `A07-01`；实践 `D<群号>-<两位序号>`）、`group`（"07"）、`related`（列表，可空）、`kind`、`name`（文件/目录名主体，不含语言后缀与扩展名，如 `Stanford_CS224N_2025Winter_Slides`，脚本自动加 `_en`）、`lang`（en/cn/…）、`title`、`instructors`、`institution`、`code`、`term`、`level`（本科基础/本科进阶/研究生核心/研究生专题）、`requirement`（必修基础/选修方向）、`prereq`（先修课，依据课程官网）、`difficulty`（入门/中级/高级）、`syllabus_url`（官方大纲/课程主页）、`syllabus_note`（大纲要点，中文 1–2 句，依据官网）、`reason`（选入理由）、`summary`（简介，注明依据：课程主页/大纲/目录）、`summary_basis`、`license`。
- 课程另加 `pack_type`；实践另加 `learning_goals`、`environment`。
- kind 参数：`url` / `urls` / `index_url` + `link_regex` + `min_files` / `min_pages` / `min_pages_each` / `title_phrase` / `skip_regex` / `repo` + `ref` + `must_contain` + `max_mb` / `src`。

## 流程
1. 逐群查官方页面（WebFetch/curl 看结构，确定讲次数与链接规律）。HTTP 请求要节制。
2. 写清单条目 → `python3 -I scripts/materials_en.py fetch courses --only A07-01`（或 practice）→ 看结果。失败就换合法来源或换课程，失败条目保留在清单里并加 `"exclude": true, "exclude_reason": "..."`（它会作为失败记录进报告）。
3. 每群至少 3 套课程、2 套实践核验通过后再做下一群；做不到的写入 `scripts/annotations/materials_gap_<分片>_cn.md`。
4. 不要修改 `scripts/*.py`、其他分片文件、兄弟库目录；不要动 `papers/`、`books/`。

## 回报
每群一行：课程核验通过数（完整文字讲义 / 完整课件包 / OCW 包分别多少）、实践核验通过数、失败数；缺口文件路径；需主会话注意的问题。
