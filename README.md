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

Chart1.py

Commit_author_stats.py

Line_connected_scatter_plot_top_50_categories.html

Top_50_contributors_treemap.html

Treemap_chart.html

##### 3.2王杰所作工作

Illustration.py 

Interpret_illustration.docx

