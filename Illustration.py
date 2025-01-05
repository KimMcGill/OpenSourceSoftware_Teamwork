import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 用于存储提取的信息
data = []

# 以utf-8编码打开文件
with open('LinuxCommitsInfo.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 提取Commit SHA
        if 'Commit SHA:' in line:
            commit_sha = line.split(': ')[1].strip()
        # 提取Message中的关键信息
        elif 'Message:' in line:
            message = line.split(': ', 1)[1].strip()
            # 进一步提取修复的模块或功能信息
            module_info = []
            if 'fix' in message.lower() or'revert' in message.lower() or 'update' in message.lower():
                parts = message.split(', ')
                for part in parts:
                    if 'fix' in part.lower():
                        module_info.append(part[part.find(' ') + 1:])
                    elif'revert' in part.lower():
                        module_info.append(part[part.find(' ') + 1:])
                    elif 'update' in message.lower():
                        module_info.append(part[part.find(' ') + 1:])
            # 将信息添加到数据列表中
            data.append({'Commit SHA': commit_sha, 'Module/Function': module_info})

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 展开Module/Function列，以便每个修复的模块或功能都有单独的行
df_exploded = df.explode('Module/Function')

# 统计每个模块或功能的修复次数
module_fix_counts = df_exploded['Module/Function'].value_counts()

# 绘制柱状图展示修复次数排名前10的模块或功能
top_10_modules = module_fix_counts.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_modules.index, y=top_10_modules.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Module/Function')
plt.ylabel('Fix Count')
plt.title('Top 10 Modules/Functions by Fix Count')
plt.show()

# 按Commit SHA分组，统计每个提交涉及的修复次数
commit_fix_counts = df_exploded.groupby('Commit SHA').size()

# 绘制箱线图展示修复次数分布
plt.figure(figsize=(12, 6))
sns.boxplot(y=commit_fix_counts)
plt.ylabel('Number of Fixes per Commit')
plt.title('Distribution of Fixes per Commit')
plt.show()

# 过滤掉Module/Function列中的float类型数据
filtered_df = df_exploded[df_exploded['Module/Function'].apply(lambda x: isinstance(x, str))]

# 统计不同类型修复（如fix、revert、update）的数量
fix_type_counts = filtered_df['Module/Function'].apply(lambda x: 'fix' if 'fix' in x.lower() else ('revert' if'revert' in x.lower() else 'update')).value_counts()

# 绘制饼图展示修复类型分布
plt.figure(figsize=(8, 8))
plt.pie(fix_type_counts.values, labels=fix_type_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Fix Types')
plt.show()
