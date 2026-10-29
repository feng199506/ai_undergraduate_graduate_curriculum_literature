# 全库核心阅读清单（core_reading_list）

> 推荐章节均已对照本地 PDF 的书签目录（pypdf outline）或目录页核实，核实日期 2026-10-29。HTML 教材按官网目录页核实。章节名保留原文，方便对照。“难度”沿用 `catalog_cn.csv`。只列全库优先的核心资料；完整清单见 catalog。

## A. 数学与基础（先读）
| 编号 | 资料 | 用途 | 难度 | 对应课程 | 推荐章节（已核实目录） |
|---|---|---|---|---|---|
| B01-03 | Deisenroth 等《Mathematics for Machine Learning》 | ML 所需数学一站式 | 中级 | A01-01、A01-03、A06-03 | Part I：2 Linear Algebra、3 Analytic Geometry、4 Matrix Decompositions、5 Vector Calculus、6 Probability and Distributions、7 Continuous Optimization；Part II 9 Linear Regression、10 PCA 作为应用练习 |
| B01-02 | Boyd–Vandenberghe《Introduction to Applied Linear Algebra》 | 计算型线代入门 | 入门 | A01-01 | I Vectors、II Matrices、III Least squares（全书三部分） |
| B02-01 | Grinstead–Snell《Introduction to Probability》 | 本科概率 | 入门 | A02-01、A01-05 | 1 Discrete Probability Distributions、2 Continuous Probability Densities、3 Combinatorics、4 Conditional Probability；9 Central Limit Theorem；11 Markov Chains；12 Random Walks |
| B03-01 | Boyd–Vandenberghe《Convex Optimization》 | 凸优化 | 中级 | A03-01、A03-02 | I Theory：Convex sets、Convex functions、Convex optimization problems、Duality；III Algorithms：Unconstrained minimization、Interior-point methods |
| B04-01 | Downey《Think Python》2e | 编程入门 | 入门 | A04-01 | 全书 1–18 章（The way of the program 至 Inheritance）；Debugging 附录 |
| B04-02 | Erickson《Algorithms》 | 算法设计 | 中级 | A04-02 | Recursion、Backtracking、Dynamic Programming、Greedy Algorithms、Basic Graph Algorithms、Depth-First Search、Shortest Paths、NP-Hardness |

## B. AI 与机器学习核心
| 编号 | 资料 | 用途 | 难度 | 对应课程 | 推荐章节（已核实目录） |
|---|---|---|---|---|---|
| B05-01 | Poole–Mackworth《AI: Foundations of Computational Agents》3e（HTML） | AI 导论主教材 | 中级 | A05-01、A05-03 | 官网目录：搜索、约束推理、命题推理、不确定性推理、规划、强化学习等章（离线包含官网全部章节页，见 PAGES_en.txt） |
| B06-01 | James 等《ISL with Applications in Python》 | ML 入门与实验 | 入门 | A06-03 | 2 Statistical Learning、3 Linear Regression、4 Classification、5 Resampling Methods、6 Linear Model Selection and Regularization、8 Tree-Based Methods、9 SVM、10 Deep Learning、12 Unsupervised Learning、13 Multiple Testing |
| B06-03 | Murphy《Probabilistic ML: An Introduction》 | 概率视角的 ML 主教材 | 中级 | A06-01 | I Foundations（2–8 章：概率、统计、决策论、信息论、线代、优化）；II Linear Models（10 Logistic Regression、11 Linear Regression）；IV 18 Trees, Forests, Bagging, and Boosting；V 20 Dimensionality Reduction、21 Clustering |
| B06-04 | Shalev-Shwartz–Ben-David《Understanding ML》 | 学习理论 | 高级 | A06-05 | Part I Foundations（A Formal Learning Model、Uniform Convergence、Bias-Complexity Tradeoff、VC-Dimension）；Part II 中 Model Selection and Validation、Convex Learning Problems、Regularization and Stability、SGD |
| B06-05 | Hardt–Recht《Patterns, Predictions, and Actions》 | 从预测到决策、数据集与因果 | 中级 | A06-01、A20-01 | Supervised learning、Optimization、Generalization、Deep learning、Datasets、Causality |
| B07-01 | Prince《Understanding Deep Learning》 | 深度学习主教材 | 中级 | A07-01、A07-03 | Supervised learning 至 Regularization（损失、拟合、梯度与初始化、性能度量、正则化）；Convolutional networks、Residual networks、Transformers；生成部分 VAE/Diffusion models 可延后到 12 群 |
| B07-02 | Zhang 等《Dive into Deep Learning》 | 代码驱动 | 入门 | A07-02、D07-01 | Preliminaries、Linear Neural Networks、Multilayer Perceptrons、Builders' Guide、CNN、Attention Mechanisms and Transformers、Optimization Algorithms、Computational Performance |
| B08-01 | Bishop《Pattern Recognition and ML》 | 概率图模型与近似推断 | 中级 | A08-01、A08-03 | 8 Graphical Models、9 Mixture Models and EM、10 Approximate Inference、11 Sampling Methods、13 Sequential Data |

## C. 方向核心
| 编号 | 资料 | 用途 | 难度 | 对应课程 | 推荐章节（已核实目录） |
|---|---|---|---|---|---|
| B09-01 | Jurafsky–Martin《Speech and Language Processing》3e 草稿 | NLP 主教材 | 中级 | A09-01、A09-03 | I：Words and Tokens、N-gram Language Models、Embeddings、Transformers and Pretraining、Post-training；II：Retrieval-based Models、Machine Translation；III：Sequence Labeling、Dependency Parsing、Information Extraction |
| B10-01 | Xiao–Zhu《Foundations of LLMs》 | LLM 原理 | 中级 | A10-01、A10-02 | Pre-training、Generative Models、Prompting、Alignment、Inference、Reasoning（全书六章） |
| B10-02 | 赵鑫等《大语言模型》 | 中文 LLM 教材 | 中级 | A10-01 | 第一部分 背景与基础知识、第二部分 预训练、第三部分 微调与对齐、第四部分 大模型使用、第五部分 评测与应用（书签目录五部分） |
| B14-01 | Lynch–Park《Modern Robotics》 | 机器人学 | 中级 | A14-02、A14-03 | Configuration Space、Rigid-Body Motions、Forward/Velocity/Inverse Kinematics、Dynamics of Open Chains、Trajectory Generation、Motion Planning、Robot Control |
| B19-01 | Reddi 等《Machine Learning Systems》卷 I | ML 系统工程 | 中级 | A19-01、A19-03 | ML Lifecycle、Data Engineering、ML Frameworks、Model Training、Model Compression、Hardware Acceleration、Benchmarking、Model Serving、ML Operations、Responsible Engineering |
| B19-02 | 同上卷 II | 大规模分布式系统 | 高级 | A19-02 | 导论后各章（通信与集合通信、并行维度与扩展效率、集群可靠性与检查点、大规模服务）以官方目录为准 |
| B18-03 | Dwork–Roth《Algorithmic Foundations of DP》 | 差分隐私 | 高级 | A18-01 | The Promise of Differential Privacy、Basic Terms、Basic Techniques and Composition Theorems、Differential Privacy and Machine Learning |
| B18-04 | Hendrycks《Introduction to AI Safety, Ethics, and Society》 | AI 安全与伦理导论 | 入门 | A18-01、A20-01 | I AI and Societal-Scale Risks、II Safety、III Ethics and Society（三部分） |
| B16-02 | Ma–Tang《Deep Learning on Graphs》 | 图深度学习 | 中级 | A16-01 | 2 Foundations of Graphs（含图傅里叶变换、复杂图、计算任务）、3 Foundations of Deep Learning；方法部分各章 |

## D. 研究方法
| 编号 | 资料 | 用途 | 难度 | 推荐部分 |
|---|---|---|---|---|
| A20-01 | Stanford CS197 Computer Science Research | 研究流程课 | 入门 | 全部讲次 |
| B20-02 | Good Research Code Handbook（HTML） | 研究代码规范 | 入门 | 官网全部页面（离线包页面清单） |
| B20-04 | Knuth 等《Mathematical Writing》 | 写作 | 中级 | 前部“写作规则”与批改示例讲次 |
| B20-03 | ORI《Responsible Conduct of Research》 | 研究伦理 | 入门 | 研究不端、数据管理、署名与发表、同行评审各章 |

## E. 第二、三轮下载后补充核实的核心书目
| 编号 | 资料 | 用途 | 难度 | 对应课程 | 推荐章节（已核实目录） |
|---|---|---|---|---|---|
| B06-02 | Hastie 等《The Elements of Statistical Learning》2e | 统计学习（研究生） | 高级 | A06-01、A06-04 | 2 Overview of Supervised Learning、3 Linear Methods for Regression、4 Linear Methods for Classification、7 Model Assessment and Selection、9 Additive Models, Trees、10 Boosting and Additive Trees、15 Random Forests |
| B13-01 | Sutton–Barto《Reinforcement Learning: An Introduction》2e | 强化学习主教材 | 中级 | A13-05、A13-01 | I Tabular Solution Methods（Multi-armed Bandits、Finite MDPs、Dynamic Programming、Monte Carlo Methods、Temporal-Difference Learning、n-step Bootstrapping、Planning and Learning）；II 中 On-policy Prediction/Control with Approximation、Policy Gradient Methods |
| B17-01 | Hernán–Robins《Causal Inference: What If》 | 因果推断主教材 | 中级 | A17-01、A17-02 | Part I Causal inference without models：1 A definition of causal effect、2 Randomized experiments、3 Observational studies（目录页核实）及其后续章节 |
| B16-01 | Hamilton《Graph Representation Learning》 | 图表示学习 | 中级 | A16-01 | Background and Traditional Approaches、I Node Embeddings、II Graph Neural Networks |
| B18-01 | Molnar《Interpretable ML》3e（HTML） | 可解释性 | 中级 | A18-01 | 离线包页面：interpretability、limo（线性模型）、tree、pdp、ale、feature-importance、lime、shapley、shap、counterfactual、pixel-attribution、evaluation |
| B18-02 | Barocas–Hardt–Narayanan《Fairness and ML》 | 公平性 | 中级 | A18-03 | Classification、Relative notions of fairness、Causality、Testing discrimination in practice、Datasets |
| B11-01 | Torralba–Isola–Freeman《Foundations of Computer Vision》（HTML） | 视觉主教材 | 中级 | A11-01、A11-05 | 离线包页面：imaging、lenses、linear_image_filtering、image_processing_fourier、sampling_and_aliasing、pyramids、convolutional_neural_nets、transformers 及后续几何与场景理解章节 |
| B05-03 | Ghallab–Nau–Traverso《Acting, Planning, and Learning》 | 规划与行动（研究生） | 高级 | A05-04 | Deterministic State-Transition Systems、Hierarchical Task Networks、Probabilistic Models、Nondeterministic Models、Temporal Models |
| B12-01 | Lai 等《The Principles of Diffusion Models》 | 扩散模型专著 | 高级 | A12-01、A12-02 | A Introduction to Deep Generative Modeling、B Foundations and Perspectives of Diffusion Models、C Sampling of Diffusion Models |

未通过核验、不在推荐范围：B20-05 Chapman（DSpace 返回 HTTP 429，三次重试均失败）；algorithmsbook.com 三本与 CASI（见 `download_failures_cn.csv`）。
