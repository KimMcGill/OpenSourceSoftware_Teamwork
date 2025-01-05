# 导入所需库
from collections import defaultdict
import re

# 定义文件路径
input_file = 'LinuxCommitsInfo.txt'
output_file = 'AuthorCommitDetails.txt'

# 初始化字典，用于存储每个作者的提交次数和内容
author_details = defaultdict(lambda: {'count': 0, 'messages': []})

# 定义正则表达式匹配 Author 和 Message 字段
author_pattern = re.compile(r'^Author:\s+(.*)$', re.MULTILINE)
message_pattern = re.compile(r'^Message:\s+(.*)$', re.MULTILINE)

# 读取文件并解析作者和提交内容
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()
    authors = author_pattern.findall(content)  # 找到所有 Author 字段
    messages = message_pattern.findall(content)  # 找到所有 Message 字段

    # 打印警告并记录不匹配信息
    if len(authors) != len(messages):
        print(f"警告：作者数量 ({len(authors)}) 和提交消息数量 ({len(messages)}) 不匹配！")
        mismatch_log = 'MismatchLog.txt'
        with open(mismatch_log, 'w', encoding='utf-8') as log_file:
            log_file.write("Authors:\n")
            log_file.writelines([f"{i + 1}: {author}\n" for i, author in enumerate(authors)])
            log_file.write("\nMessages:\n")
            log_file.writelines([f"{i + 1}: {message}\n" for i, message in enumerate(messages)])
        print(f"不匹配信息已保存到 {mismatch_log}")

    # 更新字典，统计每个作者的提交次数和内容
    for author, message in zip(authors, messages):
        author_details[author]['count'] += 1
        author_details[author]['messages'].append(message)

# 将统计结果保存到文件并打印
with open(output_file, 'w', encoding='utf-8') as file:
    file.write("Author Commit Details:\n")
    for author, details in author_details.items():
        file.write(f"\n{author}: {details['count']} commits\n")
        for message in details['messages']:
            file.write(f"  - {message}\n")

print(f"统计结果已保存到 {output_file}")

# 添加统计前五十贡献者及其贡献最多的内容
import pandas as pd
import plotly.express as px

# 转换数据为绘图所需的格式
data = []
for author, details in author_details.items():
    # 找到每位贡献者贡献最多的内容
    message_counts = defaultdict(int)
    for message in details['messages']:
        message_counts[message] += 1
    top_message = max(message_counts, key=message_counts.get, default="无内容")
    data.append({'Author': author, 'Count': details['count'], 'TopMessage': top_message})

# 按贡献次数排序，并选取前50位贡献者
data = sorted(data, key=lambda x: x['Count'], reverse=True)[:50]

# 创建DataFrame用于绘图
top_50 = pd.DataFrame(data)

# 创建树状图
fig = px.treemap(
    top_50,
    path=[px.Constant("所有贡献者"), 'Author', 'TopMessage'],  # 构建路径：所有贡献者 > 作者 > 最多贡献内容
    values='Count',
    color='Count',
    hover_data=['TopMessage'],
    color_continuous_scale='RdBu',
    title="Top 50 Contributors and Their Most Frequent Contributions",
)

# 更新布局以提高图表的可读性和外观
fig.update_layout(
    margin=dict(l=20, r=20, t=60, b=20),
    font=dict(size=14),
)

# 显示图表
fig.show()

# 将图表保存为HTML文件
output_filename = "top_50_contributors_treemap.html"
fig.write_html(output_filename)
print(f"图表已保存为 {output_filename}")
