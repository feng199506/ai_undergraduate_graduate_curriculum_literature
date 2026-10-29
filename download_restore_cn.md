# 下载与解压恢复说明（人工智能本科—研究生课程资料库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含以下内容，不含课程讲义、教材、论文、实践材料和培养方案全文：
  - 根目录的总报告与登记表：`README_cn.md`、`catalog_cn.csv`、`progress_cn.csv`、`download_failures_cn.csv`、`search_log_cn.md`；
  - `guides/`（课程体系图、学习路线、核心阅读清单、实践项目）；
  - 脚本 `scripts/`（含种子清单、检索式、状态与缓存）；
  - 本说明、分包索引、改名明细和未发布清单。

  仓库原有的 `main` 分支没有改动。这个分支的父提交是 `main`。
- **Release `aiug-full-20261029`**：9 个独立的不压缩 `.tar` 包，合起来就是资料库的发布内容。

Release 页面：https://github.com/feng199506/ai_undergraduate_graduate_curriculum_literature/releases/tag/aiug-full-20261029

## 1. 未发布的资料（仍保存在本机资料库中）

下列 6 本教材的许可声明明确限制为个人使用或仅限在线阅读，公开发布会超出许可范围，因此**没有放进 Release，也没有放进 Git 分支**。

- 它们在 `catalog_cn.csv` 中仍有登记，解压后对应路径下没有文件。
- 明细见 `release_excluded_cn.csv`。
- 这些书都可以从作者或出版社官网免费阅读或下载，地址见该文件。

| 编号 | 教材 | 许可声明（摘自 catalog_cn.csv） |
|---|---|---|
| B01-02 | Boyd & Vandenberghe《Introduction to Applied Linear Algebra》 | 作者官网免费个人使用 |
| B01-03 | Deisenroth, Faisal & Ong《Mathematics for Machine Learning》 | 作者官网免费个人使用 |
| B03-01 | Boyd & Vandenberghe《Convex Optimization》 | 作者官网免费个人使用 |
| B05-03 | Ghallab, Nau & Traverso《Acting, Planning, and Learning》 | 作者项目页公开（个人使用） |
| B06-04 | Shalev-Shwartz & Ben-David《Understanding Machine Learning》 | 作者官网个人使用免费 |
| B07-03 | Goodfellow, Bengio & Courville《Deep Learning》（离线 HTML） | 官网仅限在线阅读，离线保存仅供个人学习 |

《Bayesian Data Analysis》第 3 版（B02-03）的作者主页声明是“可免费下载用于非商业用途”，没有禁止再分发，已照常发布。

## 2. 包列表

包按路径顺序切分，内容范围如下（文件名前缀都是 `ai_undergraduate_graduate_curriculum_literature_20261029_`，后缀都是 `_cn_en.tar`）：

| 包 | 内容范围（按路径顺序） |
|---|---|
| `batch001` | 根目录报告与登记表、`scripts/`，以及 `books/` 的大部分（到 Torralba《Foundations of Computer Vision》的一部分） |
| `batch002` | `books/` 其余部分，以及 `courses/` 的开头部分（到 CMU 11-711 课件的一部分） |
| `batch003` | `courses/` 中间部分（CMU 11-711 其余课件，到 MIT 6.100L） |
| `batch004` | `courses/` 中间部分（MIT 6.172，到 Stanford CS329S 的一部分） |
| `batch005` | `courses/` 其余部分、`curricula/`、`guides/`，以及 `papers/` 的 01–08 课程群（08 的一部分） |
| `batch006` | `papers/` 08–12 课程群（12 的一部分） |
| `batch007` | `papers/` 12–18 课程群（18 的一部分） |
| `batch008` | `papers/` 其余部分，以及 `practice/` 的前一部分（到 NeuralOperator 的一部分） |
| `batch009` | `practice/` 其余部分 |

每个文件属于哪个包，见 `archive_index_cn.csv`。它是 UTF-8 带 BOM 编码，可直接用 Excel 打开，共 33,450 行，每行一个文件。

- 每个包都可以**单独解压**，不需要拼接。
- 包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包没有压缩，所需磁盘空间约等于包的大小。全部解压约需 **12.1 GiB**。
- 如果还要展开里面的 OCW 课程包等 `.zip`（见第 5 节），建议预留 20 GiB。

## 3. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击下列文件，全部保存到**同一个下载文件夹**，例如 `D:\下载\aiug\`：
   - 9 个 `.tar` 文件；
   - `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`release_excluded_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断时，可以在浏览器的下载列表里点“恢复”，或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，核对每个包的大小。在文件属性窗口里看“大小”一项的字节数，不要看“占用空间”。

## 4. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\aiug\`。

1. 在下载文件夹中，按住 Ctrl 选中 9 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\aiug\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 点确定。

也可以逐个解压：每个包都右键 → WinRAR → **解压文件…**，目标路径都填同一个 `D:\aiug\`。不要用“解压到 ai_undergraduate_graduate_curriculum_literature_20261029_batch00X_cn_en\”这个菜单项：它会给每个包各建一个子文件夹，目录结构就被拆散了，而且文件夹名很长，会让路径超出 Windows 的限制。

解压后的目录结构：

```
D:\aiug\
├─ README_cn.md、catalog_cn.csv、progress_cn.csv、download_failures_cn.csv、search_log_cn.md
├─ curricula\ courses\ books\ papers\ practice\
├─ guides\
└─ scripts\
```

### Windows 兼容处理

发布包里的文件名都已经处理过，在 Windows 下解压不会因为文件名报错，最长相对路径 166 个字符。资料库的本地原件没有改动，每一处改名和改写都逐条记在 `windows_rename_map_cn.csv` 里。

- **文件名带 Windows 不允许的字符（76 个文件）**：主要是网页离线镜像中形如 `style.css?ver=…` 的样式、脚本和字体文件。名字里的 `?` 等字符改成 `_`。
  - 主要集中在《How to Scale Your Model》（27 个）、MIT 6-4 培养方案网页（13 个）、《Good Research Code Handbook》、CMU 10-708 讲义、Python 官方教程、NYU DS-GA 1008 讲义、剑桥 MLMI 培养方案等网页离线镜像中。
- **路径过长（76 个名字截短）**：
  - 主要是 Stanford CS336 讲义仓库中按原网址命名的图片缓存（42 个），其余在 Stanford CS221、CS228 讲义和几本网页版教材的镜像中。
  - 在超过 165 个字符的路径里，最长的那一级名字被截短为“前 12 个字符 + 原名的 8 位哈希”。
  - 涉及 74 个文件名，另有 15 个文件因所在目录改名而路径变化。
- **同一目录下只差大小写的文件（1 个）**：Stanford CS231n 作业仓库中的 `assets/rnn/unrolledRNN.png`。它与同目录另一个只差大小写的文件在 Windows 下会互相覆盖，因此加了 `_case2` 后缀。
- **页面引用同步改写**：117 个网页、样式表、JSON 等文本文件中，指向这些改名文件的链接已同步改写，离线打开时仍能正常显示。
  - 改写时会逐条核对，只有确实指向已改名文件的链接才会改。
  - 改写前后全库的本地网页链接都核对过，失效链接没有增加。
- **内层归档**：59 个内层 `.zip` / `.tar`（OCW 课程包等）已逐个检查，名字里没有 Windows 不允许的字符，没有只差大小写的文件，也没有符号链接，没有改动。

## 5. 内层归档（.zip / .tar）

资料库把部分课程以官方整包保存，例如 MIT OCW 课程包 `.zip`。解压发布包之后，它们仍是单个文件，需要时再单独解开：右键该文件 → WinRAR → **解压到 “文件名\”**。

## 6. Linux / macOS

```bash
mkdir -p ~/aiug
for f in ai_undergraduate_graduate_curriculum_literature_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/aiug || echo "FAILED: $f"; done
```

## 7. 资料状态说明（来自资料库自身的报告，与打包无关）

- **只计已核验条目**：全库去重共 1,288 条，详见 `README_cn.md` 和 `catalog_cn.csv`：
  - 课程 76、教科书/参考书 79；
  - 论文、综述与学术教程 1,064（近三年占 92.0%）；
  - 官方实践材料 52、培养方案参考 16。

  其中 6 本教材属于第 1 节的未发布资料。
- **失败、残缺、排除与待核验记录 38 条**：记录在 `download_failures_cn.csv`，不计入。
- **快照时间**：本次按 2026-10-29 22:30（中欧时间）的资料库内容打包。打包前先把整个资料库复制成一份快照，打包用的就是这份快照。资料库最后一次写入是在 22:16。

## 8. 完整性说明

- 本次发布只登记了上传状态：GitHub API 显示附件为 `uploaded`，且远端大小等于本地大小。**没有**做下载回验和哈希校验。
- `catalog_cn.csv` 的 SHA256 列是下载当时记录的单文件值。改名或改写过的文件，以发布包中的为准。
- 除第 1 节的未发布资料外，资料库中的资料文件都已打包。另外只排除了：
  - 本地 `.git/`，约 3.9 MB；
  - `scripts/__pycache__/` 等处的 10 个 `.pyc`。
- 16 个 `uv.lock`、`poetry.lock`、`yarn.lock`、`Gemfile.lock` 是项目依赖锁文件，属于资料内容，已打包。
