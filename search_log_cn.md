# 检索日志（search_log）

检索日：2026-10-29。近三年窗口：首次公开日（arXiv v1）在 2023-10-29 至 2026-10-29 之间。

## 一、检索来源与方法
| 资料类别 | 来源 | 方法 |
|---|---|---|
| C 论文、综述、学术教程 | arXiv 官方 API（export.arxiv.org）检索与元数据；少量为 arXiv 已知 ID 的直接元数据查询 | 每群 12–32 条检索式（标题/摘要关键词 + 综述/教程/讲义词），按相关度取前 30–60 条，自动附加日期窗口；候选由人工按“教学价值、与课程群内容直接相关、综述/教程优先、代表性研究与基准”筛选；三年前经典每群 ≤5 条并写理由 |
| A 课程 | 各大学课程官网、MIT OpenCourseWare 官方整包、教师主页、官方 GitHub 仓库 | 先人工查看课程日程页确认讲次数，再按官方索引页抓取全部讲次（缺讲次即不计） |
| B 教材 | 作者主页、出版社开放获取页、官方 GitHub Release、arXiv 作者版 | 优先作者/出版社官方全文；核对书名与页数；HTML 版按官网目录保存全部页面 |
| D 实践 | 官方课程作业仓库、官方教程仓库、官方文档 | git ls-remote 解析提交号后下载该提交的归档；记录学习目标、环境、许可证 |
| 培养方案参考 | 各校官方学位要求页、官方目录 PDF、研究生院附件、ACM/IEEE/AAAI CS2023 | 保存页面或 PDF；仅作参考，不计入教材/课程 |

## 二、不可用或受限的数据源（如实记录）
- Semantic Scholar API：HTTP 429（无 API key，同 IP 额度用尽）；OpenAlex：当日免费额度用尽。因此未用引用数排序，改为人工判断。
- arXiv：与本机另外两个文献库共用同一限速锁（每 5 秒 1 次请求），并发检索期间下载约每分钟 1 篇。
- algorithmsbook.com（Kochenderfer 等三本书）：PDF 地址返回脚本验证页（反爬校验），按规则不绕过，未收。
- hastie.su.domains 的 CASI 全文 PDF：原链接 404，未收。
- nlp.stanford.edu、web4.cs.ucl.ac.uk、www.cds.caltech.edu、infolab.stanford.edu、cs.stanford.edu：从本机无法连接，相关资料（IIR、Barber BRML、Prince CVMLI、MLS、MMDS、斯坦福 MSCS AI 方向表）未收或换替代来源。
- CMU 15-213 各学期课程页需要 CMU 登录，未收；MIT 6.7960 课件存放于 Dropbox（约 700 MB）、CMU 11-785 课程页由脚本渲染，未收。
- 机器学习深度学习兄弟库（/root/machine_learning_deep_learning_literature）在本轮执行中从本机消失（非本流程删除），原计划“已有复用”的约 40 本教材与约 20 套课程改为从官方来源重新下载并核验。

## 三、筛选与排除规则（摘要）
- 排除：博客、新闻、宣传页；作者撤回或 arXiv 管理员标注大段文本重叠的论文（如 2412.16543、2408.16002、2407.01456）；仅摘要/残缺全文；与课程群教学内容关联弱的纯应用论文。
- 跨群重复：同一论文只计入编号最小的课程群，其他群的同一条目不计数（目录“交叉课程群”列记录关联）。
- 同一研究不同版本只收最新版本（arXiv 最新版），首次公开日按 v1 记；同一本书不同版本、同一课程不同学期只收一个。
- 简介只依据 arXiv 摘要或作者/出版方简介与目录，不声称读过全文。

## 各课程群检索统计（由脚本生成）

| 群 | 检索式条数 | 候选（去重 arXiv ID） | 候选中近三年 | 种子（主列表/后备） | 已核验 | 待核验 | 失败 | 跨群让出/修订移出 |
|---|---|---|---|---|---|---|---|---|
| 01 数学基础 | 42 | 370 | 370 | 45/8 | 51 | 0 | 2 | 0 |
| 02 概率与统计 | 32 | 373 | 373 | 52/8 | 51 | 0 | 1 | 0 |
| 03 优化与信息论 | 36 | 612 | 612 | 54/9 | 51 | 0 | 3 | 1 |
| 04 计算机科学与编程基础 | 33 | 425 | 425 | 54/10 | 52 | 0 | 2 | 0 |
| 05 人工智能基础 | 26 | 707 | 707 | 54/9 | 54 | 0 | 0 | 1 |
| 06 机器学习 | 32 | 694 | 694 | 54/8 | 54 | 0 | 0 | 3 |
| 07 深度学习 | 21 | 627 | 627 | 55/8 | 54 | 0 | 1 | 0 |
| 08 概率图模型与概率机器学习 | 29 | 637 | 637 | 54/8 | 53 | 0 | 1 | 0 |
| 09 自然语言处理 | 17 | 511 | 511 | 55/9 | 54 | 0 | 0 | 1 |
| 10 大语言模型与智能体 | 18 | 660 | 660 | 55/9 | 54 | 0 | 1 | 0 |
| 11 计算机视觉 | 18 | 433 | 433 | 55/8 | 54 | 0 | 1 | 0 |
| 12 生成模型与多模态学习 | 19 | 463 | 463 | 55/9 | 53 | 0 | 2 | 0 |
| 13 强化学习与控制 | 20 | 626 | 626 | 54/9 | 51 | 0 | 3 | 0 |
| 14 机器人与具身智能 | 18 | 450 | 450 | 56/10 | 53 | 0 | 3 | 0 |
| 15 时间序列与信号处理 | 19 | 290 | 290 | 55/8 | 53 | 0 | 2 | 0 |
| 16 图学习与推荐系统 | 20 | 626 | 626 | 54/10 | 52 | 0 | 2 | 0 |
| 17 因果推断与科学机器学习 | 23 | 458 | 458 | 55/10 | 55 | 0 | 0 | 0 |
| 18 可信人工智能 | 18 | 568 | 568 | 54/8 | 54 | 0 | 0 | 0 |
| 19 人工智能系统与部署 | 20 | 734 | 734 | 56/10 | 55 | 0 | 1 | 0 |
| 20 研究方法与综合实践 | 18 | 636 | 636 | 56/10 | 56 | 0 | 0 | 0 |

## 检索式全文

各群检索式见 `scripts/seeds/queries/NN_en.json`（字段 q 为 arXiv search_query，subtopic 为子主题；未标 old 的检索式自动附加日期窗口 submittedDate:[20231029 TO 20261029]）。示例（每群前 3 条）：

- **01 数学基础**：`(ti:tutorial OR ti:primer OR ti:introduction OR ti:"lecture notes") AND abs:"linear algebr`（线性代数与 ML 数学基础）；`abs:"matrix calculus" OR ti:"matrix calculus"`（矩阵微积分）；`(ti:survey OR ti:review OR ti:tutorial OR ti:"lecture notes") AND abs:"randomized numerica`（随机数值线性代数）
- **02 概率与统计**：`(ti:tutorial OR ti:introduction OR ti:"gentle introduction" OR ti:primer) AND abs:"conform`（共形预测）；`(ti:survey OR ti:review) AND abs:"conformal prediction"`（共形预测）；`(ti:"statistical significance" OR ti:"statistical tests" OR ti:"hypothesis testing" OR ti:`（ML 评测中的统计检验）
- **03 优化与信息论**：`(ti:tutorial OR ti:introduction OR ti:"lecture notes" OR ti:primer OR ti:course) AND (abs:`（凸优化）；`(ti:survey OR ti:review OR ti:tutorial) AND (abs:"first-order methods" OR abs:"gradient me`（一阶方法与数值优化）；`(ti:survey OR ti:review OR ti:tutorial OR ti:introduction) AND abs:"stochastic gradient" A`（随机优化）
- **04 计算机科学与编程基础**：`(ti:survey OR ti:review OR ti:tutorial) AND (abs:"software engineering for machine learnin`（ML 软件工程）；`(ti:"technical debt" OR ti:"code smells" OR ti:"bugs") AND (abs:"machine learning" OR abs:`（ML 软件质量与缺陷）；`(ti:"learned index" OR ti:"learned indexes" OR ti:"learned database" OR ti:"machine learni`（学习型索引与数据库 ML）
- **05 人工智能基础**：`(ti:survey OR ti:review OR ti:tutorial) AND abs:"heuristic search"`（搜索算法）；`abs:"heuristic search" AND (abs:"large language model" OR abs:"learned heuristic") AND cat`（搜索算法）；`abs:"Monte Carlo tree search" AND (ti:survey OR ti:review OR abs:planning) AND cat:cs.AI`（搜索算法）
- **06 机器学习**：`(ti:"kernel methods" OR ti:"kernel ridge" OR ti:"reproducing kernel") AND (ti:survey OR ti`（核方法）；`abs:"kernel methods" AND (abs:"random features" OR abs:Nystrom OR abs:"neural tangent") AN`（核方法）；`(ti:"gradient boosting" OR ti:"decision tree" OR ti:"random forest" OR ti:"tree ensembles"`（树模型与梯度提升）
- **07 深度学习**：`(ti:survey OR ti:review) AND abs:"automatic differentiation"`（自动微分）；`(ti:tutorial OR ti:primer OR ti:introduction OR ti:"lecture notes") AND abs:"deep learning`（深度学习教程）；`(ti:survey OR ti:review) AND abs:transformer AND abs:architecture AND cat:cs.LG`（网络结构）
- **08 概率图模型与概率机器学习**：`(ti:"graphical models" OR ti:"probabilistic graphical" OR ti:"factor graph") AND (ti:surve`（概率图模型）；`abs:"probabilistic graphical models" AND (abs:"deep learning" OR abs:"neural") AND cat:sta`（概率图模型）；`(ti:"variational inference" OR ti:"variational Bayes") AND (ti:survey OR ti:review OR ti:t`（变分推断）
- **09 自然语言处理**：`(ti:survey OR ti:review OR ti:tutorial) AND abs:"computational linguistics" AND cat:cs.CL`（语言学基础与计算语言学）；`(ti:survey OR ti:review) AND (abs:syntax OR abs:"syntactic parsing" OR abs:"dependency par`（语言学基础与计算语言学）；`(ti:survey OR ti:review OR ti:primer) AND (abs:tokenization OR abs:"subword") AND cat:cs.C`（文本表示与分词）
- **10 大语言模型与智能体**：`ti:survey AND abs:"large language models" AND abs:pretraining AND cat:cs.CL`（预训练与大模型概述）；`(ti:survey OR ti:review) AND (abs:"instruction tuning" OR abs:"supervised fine-tuning") AN`（指令微调）；`(ti:survey OR ti:review) AND abs:"parameter-efficient fine-tuning"`（参数高效微调）
- **11 计算机视觉**：`(ti:survey OR ti:review) AND (abs:"image restoration" OR abs:"image super-resolution" OR a`（图像处理）；`(ti:survey OR ti:review OR ti:tutorial) AND (abs:"3D reconstruction" OR abs:"structure fro`（视觉几何）；`(ti:survey OR ti:review OR ti:tutorial) AND (abs:"neural radiance fields" OR abs:NeRF)`（视觉几何）
- **12 生成模型与多模态学习**：`(ti:tutorial OR ti:introduction OR ti:primer) AND abs:"diffusion models"`（扩散模型）；`(ti:survey OR ti:review) AND abs:"diffusion models" AND cat:cs.LG`（扩散模型）；`(ti:survey OR ti:review OR ti:tutorial OR ti:guide) AND abs:"flow matching"`（流匹配）
- **13 强化学习与控制**：`(ti:survey OR ti:review OR ti:tutorial) AND ti:"reinforcement learning"`（强化学习综述与教程）；`(ti:tutorial OR ti:introduction OR ti:primer OR ti:"lecture notes") AND abs:"reinforcement`（强化学习综述与教程）；`abs:"dynamic programming" AND abs:"Markov decision process" AND (ti:survey OR ti:tutorial `（动态规划与马尔可夫决策过程）
- **14 机器人与具身智能**：`(ti:survey OR ti:review) AND (ti:"embodied AI" OR ti:"embodied intelligence" OR ti:"embodi`（具身智能综述）；`(ti:"vision-language-action" OR ti:VLA) AND (ti:survey OR ti:review)`（视觉-语言-动作模型）；`abs:"vision-language-action" AND cat:cs.RO`（视觉-语言-动作模型）
- **15 时间序列与信号处理**：`(ti:survey OR ti:review OR ti:tutorial) AND abs:"signal processing" AND (abs:"machine lear`（信号处理与机器学习）；`(ti:tutorial OR ti:primer OR ti:"lecture notes") AND (abs:"signal processing" OR abs:"Four`（信号处理基础）；`(ti:survey OR ti:review) AND abs:"time series forecasting"`（时间序列预测）
- **16 图学习与推荐系统**：`ti:"graph neural network" AND (ti:survey OR ti:review OR ti:tutorial OR ti:introduction)`（图神经网络综述与教程）；`(ti:"graph representation learning" OR ti:"graph embedding" OR ti:"network embedding") AND`（图表示学习）；`ti:expressive* AND abs:"graph neural network" AND (ti:survey OR ti:review OR abs:Weisfeile`（GNN 表达能力）
- **17 因果推断与科学机器学习**：`(ti:"causal inference" OR ti:causality) AND (ti:survey OR ti:review OR ti:tutorial OR ti:i`（因果推断基础）；`(ti:"causal discovery" OR ti:"causal structure learning") AND (ti:survey OR ti:review OR t`（因果发现）；`(ti:"causal discovery" OR ti:"structure learning") AND (abs:DAG OR abs:"acyclic") AND cat:`（因果发现）
- **18 可信人工智能**：`(ti:survey OR ti:review) AND abs:"explainable" AND cat:cs.LG`（可解释性）；`(ti:survey OR ti:review OR ti:primer OR ti:tutorial) AND abs:"mechanistic interpretability`（机制可解释性）；`(ti:"sparse autoencoders" OR ti:"circuit") AND abs:interpretability AND cat:cs.LG`（机制可解释性）
- **19 人工智能系统与部署**：`(ti:"distributed training" OR ti:parallelism OR ti:"parallel training") AND (ti:survey OR `（分布式训练与并行）；`(abs:"pipeline parallelism" OR abs:"tensor parallelism" OR abs:"sequence parallelism" OR a`（分布式训练与并行）；`(ti:"efficient" OR ti:inference) AND (ti:"large language model" OR ti:LLM OR ti:LLMs) AND `（推理优化综述）
- **20 研究方法与综合实践**：`abs:reproducibility AND abs:"machine learning research"`（可复现性）；`(ti:reproducibility OR ti:replicability) AND cat:cs.LG`（可复现性）；`(ti:evaluation OR ti:benchmarking) AND abs:"statistical significance" AND cat:cs.LG`（ML 评测规范与统计严谨性）

## 缺口说明文件

- `scripts/annotations/01_gap_cn.md`
- `scripts/annotations/20_gap_cn.md`
- `scripts/annotations/materials_gap_g01_10_cn.md`
- `scripts/annotations/materials_gap_g11_20_cn.md`
