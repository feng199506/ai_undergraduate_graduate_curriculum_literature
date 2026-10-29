# 分片 g11_20（课程群 11–20）缺口与说明

检索日 2026-10-29。每群都已达到"≥3 套课程、≥2 套实践核验通过"的要求，没有硬缺口。下面记录被排除或放弃的候选，以及需要主会话注意的判定口径。

## 一、清单内的失败或排除记录（exclude）
- A11-02 CMU 16-385 Spring 2020：最后一讲 lecture29a.pdf 官方链接 HTTP 404，课件包不完整。已改收同一课程的 Spring 2019 版（A11-05，26 讲全部可用）。
- A13-02 Stanford CS234 Winter 2026：第 16 讲课前、课后两版 PDF 均 HTTP 404；lecture10pre 和两份客座课件也是 404。已改收 UCL David Silver RL（A13-05）。
- A20-02 Harvard CS197 课程书：Google Doc 导出 PDF 只有 16 页（多标签文档只导出首个标签），不完整。已改收主页上逐讲的 15 篇讲义（A20-04，覆盖第 1–21 讲）。
- D20-04 Harvard CS197 作业：作业 1、作业 3 的共享文档 HTTP 410（已删除），作业集不完整，已排除。第 20 群另有 D20-01/02/03 三套实践。

## 二、核验时放弃的候选（未写入清单）
- Stanford CS236（Fall 2023）：第 1、13、14、16 讲只有 PPTX，PDF 课件包不完整；notes 站也只覆盖部分主题。
- Michigan EECS 498/598（Justin Johnson）：web.eecs.umich.edu 本机连接超时，无法访问。
- Cornell CS5670、Toronto CSC2412、Harvard CS208：站点返回 HTTP 403。
- Stanford CS276（2019 页面）：新旧学期的 PPT/PDF 混杂，无法确认每讲一份完整 PDF。
- Waterloo CS 860（Kamath，Fall 2020，差分隐私）：第 16 讲只指向他人讲义，第 18、19 讲为 N/A，不完整。
- CMU 10-414/714 DLSys（Fall 2026 站点）：课程进行中，第 17、19、20、22、23 讲无课件。作业仓库 hw1、hw3 已作为实践收入（D19-01/02）。
- CMU 11-868 LLM Systems（Spring 2025 与 Spring 2026）：两个学期都有 "Efficient RL System for LLMs" 一讲没有课件。
- MIT 6.5940 EfficientML（Fall 2024）：课件放在 Dropbox，单讲约 320 MB（Lec01），整包体量过大；efficientml.ai 当时返回 522。
- Intro to ML Safety：没有官方 PDF。A18-01 是用课程主页上的 Google Slides 公开共享链接导出 PDF 得到的（Google 的标准导出接口，未绕过任何访问限制）。CS 329S（A19-01）的 Google Docs/Slides、Stanford CS197 第 0 讲和 Harvard CS197 课程书也是同样做法。

## 三、判定口径（请主会话知悉）
- 只按"教师讲授讲次"判断完整性的课程：A12-02 MIT 6.S978（其余课次为学生论文研讨）、A19-02 UW CSE 599W（客座报告无课件，第 2 讲是 notebook 实验）、A19-01 CS 329S（客座与教程课件未收；ML 基础设施一讲只有幻灯片、没有讲义）。
- A14-03 Freiburg SS 2023：日期为 FIXME 的占位行（3D Mapping 无课件；Multi-Robot Exploration、Information Driven Exploration、Summary 链接 404）视为本学期未开讲，用 skip_regex 排除。全部有日期的 20 讲都已收齐。
- D14-02 Freiburg 练习：sheet11.pdf 官方链接 404，未收；它的解答 sheet11sol.pdf 已收。
- A16-01 CS224W：当前 Fall 2026 站点仍在进行中，所以改收已完结的 Fall 2025 存档站（20 份课件）。
- 兄弟库 /root/machine_learning_deep_learning_literature 已从本机消失，原计划复用的 CS231n notes 和 MIT 6.S184 已改为从官方源直接下载（A11-01 html、A12-01 pdfs）。工业库的 EE363（A13-04）、6.011（A15-01）已复用并核验通过。
