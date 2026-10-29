# 论文选题规范（课程群 C 类资料：论文、综述与学术教程）

库根目录：`/root/ai_undergraduate_graduate_curriculum_literature`（下称 LIB）。所有命令在 LIB 下运行，Python 一律 `python3 -I`。
检索日 2026-10-29；近三年窗口 = 首次公开日（arXiv v1）在 2023-10-29 至 2026-10-29 之间。

## 目标（每群）
- 主列表约 52–55 条 + 后备 8–10 条（`"reserve": true`，主列表下载失败时按顺序补位）。下载只计核验通过的全文，所以主列表略多于 50。
- 主列表中三年前（v1 < 2023-10-29）的必要经典 **最多 5 条**，每条写 `classic_reason`（为什么非它不可）。近三年占比须 ≥ 90%。
- 内容定位：这是 AI 本科—研究生**系统学习**资料库。优先：综述（survey/review）、学术教程（tutorial/primer/lecture notes/monograph 式长文）、该子方向公认的里程碑研究论文、重要基准/评测论文。约一半综述/教程、一半代表性研究即可。
- 只收与该课程群教学内容直接相关的资料。数学（01）、计算机基础（04）等基础群若近年合适论文不足 50，**宁缺毋滥**：在 `scripts/annotations/NN_gap_cn.md` 写明缺口与原因，不为凑数收无关论文。
- 不收：博客、新闻、宣传页、纯应用领域论文（如"××在交通中的应用综述"这类与课程教学关联弱的）、撤稿/作者撤回、只有摘要的条目、超出本群范围的论文。

## 工作步骤
1. 写检索式 `scripts/seeds/queries/NN_en.json`：列表，元素 `{"q": "<arXiv search_query>", "subtopic": "<中文子主题>"}`，覆盖本群全部子主题（见下文群定义），一般 12–20 条。语法示例：`ti:survey AND abs:"graph neural network"`，`(ti:tutorial OR ti:primer OR ti:introduction) AND abs:"reinforcement learning"`，`abs:"flow matching" AND cat:cs.LG`。日期窗口由脚本自动追加；若某条要检索经典（不加窗口）写 `"old": true`。
2. 运行 `python3 -I scripts/papers_en.py search NN`（走共享限速锁，arXiv 每 5 秒一请求，耐心等；429 会自动退避）。
3. 浏览候选：`python3 -I scripts/papers_en.py show NN --abs 300`（只列窗口内；`--all` 含窗口外）。也可以加入你确知的重要论文 arXiv ID：先 `python3 -I scripts/papers_en.py meta ID1 ID2 ...` 取官方元数据，**以返回的标题、日期为准**，不要凭记忆填标题或日期。
4. 写种子 `scripts/seeds/papers/NN_<slug>_seed_cn.json`（slug 见下表），JSON 列表，**列表顺序 = 建议阅读顺序**（先综述/教程，再里程碑研究，再前沿专题）。每条字段：
   - `arxiv`：arXiv ID（不带版本号）。非 arXiv 的官方开放 PDF（如 JMLR/PMLR/会议官方库）改填 `pdf_url`、`title`、`authors`（列表）、`date`（首次公开 YYYY-MM-DD）、`date_basis`、`venue`、`landing`。
   - `subtopic`：中文子主题（与检索式子主题一致）。
   - `type`：`综述` / `学术教程` / `原始研究论文` / `基准与数据集` / `立场与方法论` 之一。
   - `level`：`本科进阶` / `研究生核心` / `研究生专题`。
   - `difficulty`：`入门` / `中级` / `高级`。
   - `reason`：选入理由（中文 1 句，说明在课程学习中的用途）。
   - `summary`：简介（中文 2–3 句，**只依据 arXiv 摘要**，用"作者称/摘要称"等措辞，不声称读过全文、不编造实验数字）。
   - `summary_basis`：固定写 `arXiv 摘要；未读全文`。
   - `classic_reason`：仅三年前条目需要。
   - `reserve`：后备条目写 `true`。
   - 可选 `related`：相关的其他课程群编号列表，如 `["07","12"]`。
5. 运行 `python3 -I scripts/papers_en.py check NN`，直到 `problems 0`。输出中 `CLAIMED-BY-xx` 表示该论文已被编号更小的群收录（本群不计数），请换一篇，避免跨群重复。
6. **不要运行 download**（由主会话集中下载）。不要改动 `scripts/*.py`、其他群的文件、兄弟库目录。

## 课程群定义（编号 / slug / 范围）
| 编号 | slug | 范围 |
|---|---|---|
| 01 | math_foundations | 线性代数、矩阵分析、微积分、多元分析、离散数学、数值计算（偏 AI 关联：矩阵计算/张量、随机数值线代、自动微分数学、数值方法在 ML 中的应用、ML 所需数学的教学型综述） |
| 02 | probability_statistics | 概率论、统计推断、随机过程、贝叶斯统计、实验设计与统计检验（含 ML 评测中的统计检验、A/B 与多重检验、共形/置信方法等教学价值高的内容） |
| 03 | optimization_information_theory | 凸优化、数值优化、随机优化、信息论及其 ML 应用 |
| 04 | cs_programming_foundations | Python、数据结构与算法、计算机系统、数据库、软件工程、并行编程（偏 AI/ML 关联：ML 软件工程、学习型索引/数据库与 ML、GPU 并行编程入门、算法与 ML 等） |
| 05 | ai_foundations | 搜索、约束满足、知识表示、逻辑推理、不确定性推理、规划与决策（含神经符号、LLM 与经典规划/搜索结合） |
| 06 | machine_learning | 监督/无监督学习、核方法、树模型、集成学习、模型选择与泛化 |
| 07 | deep_learning | 自动微分、网络结构、优化、正则化、表示学习、训练与调试 |
| 08 | probabilistic_graphical_models | 图模型、推断、变分方法、采样（MCMC/SMC）、概率编程、高斯过程、贝叶斯深度学习 |
| 09 | natural_language_processing | 语言学基础、文本表示、序列建模、机器翻译、信息抽取、多语言处理（大模型训练/对齐/智能体归 10） |
| 10 | llm_agents | 预训练、微调、对齐、推理、RAG、工具调用、代码模型、智能体及其评测 |
| 11 | computer_vision | 图像处理、视觉几何、识别、检测、分割、视频理解、三维视觉 |
| 12 | generative_multimodal | VAE、GAN、扩散、流匹配、跨模态表示、多模态理解与生成 |
| 13 | reinforcement_learning_control | 动态规划、强化学习、离线 RL、模型式 RL、最优控制、决策 |
| 14 | robotics_embodied_ai | 运动学、定位、感知、规划、控制、视觉-语言-动作模型 |
| 15 | time_series_signal_processing | 信号处理、时间序列分析、预测、状态空间、异常检测、时空建模 |
| 16 | graph_learning_recommender | 图表示、图神经网络、推荐、排序及评测 |
| 17 | causal_inference_sciml | 因果图、干预、反事实、物理约束、机理融合、科学计算应用 |
| 18 | trustworthy_ai | 可解释性、鲁棒性、不确定性、公平性、安全、隐私、数据治理 |
| 19 | ai_systems_deployment | 分布式训练、推理优化、GPU 计算、模型服务、MLOps、监控、回归测试、版本管理 |
| 20 | research_methods_practice | 文献阅读、研究问题设计、基线与消融、可复现性、学术写作、研究伦理、毕业项目方法（ML 研究方法论/可复现性/评测规范/基准设计/数据集文档化等元研究论文） |

## 完成后的回报（给主会话）
每群一行：种子总数、主列表数、后备数、主列表三年前条数、`check` 的 problems 数；缺口说明文件路径（若有）；任何你认为需要主会话注意的问题。不要贴种子全文。
