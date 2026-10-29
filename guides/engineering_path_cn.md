# 工程实践路线（engineering_path）

> 目标：从数据处理到训练、评测、服务部署、监控与维护的完整工程能力。依据本库 04、07、10、19、20 群资料；各校方案中的工程环节（清华 AI+X 与研究实践、哈工大“AI 软件开发与实践/智能系统设计与实践”、CMU MSML 的 ML in Practice 与 practicum、南开专业学位）说明工程能力是正式培养要求，见 `curriculum_map_cn.md`。

## 阶段 0：工程基本功
| 能力 | 资料 |
|---|---|
| 命令行、Shell、Git、调试、元编程 | A20-03 Missing Semester |
| Python 语言与标准库 | A04-01 6.100L、B04-01 Think Python、D04-02 Python 官方教程 |
| 软件工程实践（代码评审、测试、依赖、CI/CD） | B04-05 Software Engineering at Google |
| 研究代码规范（项目结构、可安装包、测试、文档） | B20-02 Good Research Code Handbook |
| 操作系统与并发 | B04-04 OSTEP；性能工程 A04-04 MIT 6.172 |
| 数据库与存储 | A04-03 CMU 15-445、D04-01 BusTub |

## 阶段 1：数据处理与特征
- NumPy/pandas 数据操作：D01-01 NumPy 教程；D02-01 Data 8 教材 notebook。
- 表格数据建模与验证流程（交叉验证、管道、泄露防范）：D06-01 scikit-learn MOOC、D06-02。
- 数据集文档化与治理：20 群 P 编号中的 Datasheets 等条目；18 群数据治理条目。

## 阶段 2：训练与调试
| 主题 | 资料 |
|---|---|
| 从零实现自动微分与训练循环 | D07-03 Zero to Hero、B07-04 Scardapane（自动微分）、D19-01 CMU DLSys 作业 1（needle 框架） |
| 系统化训练与调参 | B07-02 d2l（含计算性能章节）、D07-01、D07-02 UvA 教程 |
| 训练稳定性与诊断 | 07 群论文（初始化、归一化、学习率与优化器条目在 03 群） |
| 大模型训练系统（并行、显存、通信） | B19-03 How to Scale Your Model、B19-02 MLSys 卷 II、D10-02 CS336 作业 2（剖析、FlashAttention、分布式）、19 群论文（Megatron-LM、ZeRO、FlashAttention 等） |
| GPU 与并行编程 | B19-04 perfbook（并行编程通用原理）、D19-02 DLSys 作业 3（NDArray 后端）、04 群论文（KernelBench、TritonBench、ParEval 等） |

## 阶段 3：评测与回归测试
- 评测设计：20 群（评测陷阱、统计严谨性、基准批判）、02 群（统计检验、预测驱动推断等）。
- ML 测试与缺陷：04 群（ML 测试综述、DL 库测试、ML 缺陷实证、技术债）。
- LLM 与智能体评测：10 群评测条目。
- 安全关键验证：18 群鲁棒性与验证条目。

## 阶段 4：模型服务与推理优化
| 主题 | 资料 |
|---|---|
| ML 系统设计（需求、数据、部署、监控） | A19-01 Stanford CS329S、B19-01 MLSys 卷 I |
| 推理加速（量化、KV cache、投机解码、服务调度） | 19 群论文（vLLM/PagedAttention、投机解码等）、A19-02 UW CSE 599W |
| 端到端产品化 | A19-03 Full Stack Deep Learning 2022、D19-03 Made With ML |

## 阶段 5：MLOps、监控与版本管理
- 实验跟踪、数据/模型版本、CI/CD、监控与漂移检测：D19-03 Made With ML；B19-01 MLSys 卷 I 的部署与运维章节（以实际目录为准）；19 群 MLOps 与监控条目。
- 可复现性：B20-01 The Turing Way（可复现研究指南）、D20-01 代码完整性清单。

## 阶段 6：可信与合规
- 可解释性工具：D18-02 Captum；公平性：D18-03 Fairlearn；差分隐私训练：D18-04 Opacus。
- 理论背景：B18-01 Molnar、B18-02、B18-03。

## 建议的工程能力里程碑
1. 用 Git + 测试 + 可安装包组织一个小型 ML 项目（阶段 0–1）。
2. 在 needle（D19-01）或 CS336 作业 1（D10-01）中实现自动微分、模块与优化器（阶段 2）。
3. 为一个模型建立评测集、统计检验与回归测试（阶段 3）。
4. 把模型封装为服务，做批处理与延迟测试，加入监控与模型版本（阶段 4–5）。
5. 加入可解释性与公平性报告（阶段 6）。

配套项目的输入、产出与评价方式见 `practice_projects_cn.md`。本轮只整理，不执行项目。
