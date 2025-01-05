## **开源软件基础大作业**

---

### **主要任务**

* 完成分析Linux提交历史信息的分析
---

### **小组成员**

* 包明瀚
* 殷智
* 王杰
* 梁瑞洋
* 向嘉桐

---

### **项目结构及功能**

#### 1.数据爬取

Linux_commit_work.py

通过GitHub API分页获取Linux仓库的Linus  Torvalds所有提交记录并保存到文本文件中

LinuxCommitsInfo.txt

每个提交信息包括以下部分：SHA值、作者、日期、详细改动列表、关于提交消息

#### 2.数据清洗

Category_counts.csv

Category_counts.py

#### 3.数据分析与可视化

##### 3.1殷智所作工作

Chart1.py：
加载数据：读取 CSV 文件并筛选前 50 个类别。
多种可视化图表：
树状图：展示类别的层级结构及数量大小。
水平条形图：展示类别的具体数量。
带连线的散点图：显示类别数量的趋势及排名分布。
结果保存与显示：保存图表为 HTML 文件，便于交互式查看和分享。使用 matplotlib 显示条形图。

Commit_author_stats.py：
文本解析与统计: 从提交日志中提取并统计每位作者的贡献信息。
校验与记录: 检查数据完整性，提供问题文件记录。
数据可视化: 使用树状图展示前 50 名贡献者的贡献次数及最常提交的内容。
文件输出: 将统计和图表结果保存到文件，便于后续查看和分析。

Line_connected_scatter_plot_top_50_categories.html：
在chart1.py中生成，其中保存了一个带有连线的散点图，可在浏览器中打开进行交互式查看。

Top_50_contributors_treemap.html:
Commit_author_stats.py生成
贡献者分析：
帮助了解项目中前 50 位贡献者的总体贡献情况。
查看哪些贡献者提交次数最多以及他们的主要贡献方向。
数据呈现：
提供一种直观的方式，用于团队内部或报告中展示贡献者的贡献详情。
决策支持：
通过分析贡献者数据，为优化团队协作、评估成员贡献提供支持。

Treemap_chart.html:
chart1.py生成
类别分析：
帮助用户快速识别数据集中前 50 个高频类别及其分布情况。
数据呈现：
为用户提供一种简单直观的方式，在报告或演示中展示类别分布。
决策支持：
根据类别的重要性（出现次数），帮助用户优化资源分配或分析类别相关的行为模式。

MismatchLog.txt：
Commit_author_stats.py生成
Author 和 Message 的完整列表及其顺序。

AuthorCommitDetails.txt：
Commit_author_stats.py生成
每个作者的提交次数及提交内容。

##### 3.2王杰所作工作

Illustration.py 

Interpret_illustration.docx

