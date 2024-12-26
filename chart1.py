import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import os
import plotly.graph_objects as go
#取前五十出现次数最多的进行多种可视化图像
# 读取CSV文件
data = pd.read_csv('category_counts.csv')

# 获取前50个出现次数最多的类别
top_50 = data.nlargest(50, 'Count')


import plotly.express as px

# 假设top_50是一个pandas DataFrame，其中包含两个列：'Category'和'Count'

# 创建树状图
fig = px.treemap(top_50, path=[px.Constant("所有类别"), 'Category'], values='Count',
                 color='Count', hover_data=['Category'],
                 color_continuous_scale='RdBu',  # 设置颜色渐变
                 title="Top 50 Categories by Count")

# 更新布局以提高图表的可读性和外观
fig.update_layout(
    margin=dict(l=20, r=20, t=60, b=20),  # 调整边距
    font=dict(size=14),  # 增大字体大小
)

# 显示图表
fig.show()

# 将图表保存为HTML文件
output_filename = "treemap_chart.html"
fig.write_html(output_filename)
print(f"图表已保存为 {output_filename}")


# 设置Seaborn样式
sns.set(style="whitegrid")

# 绘制带有调色板的水平条形图
plt.figure(figsize=(12, 8))
sns.barplot(x='Count', y='Category', data=top_50, palette='viridis')
plt.title('Top 50 Categories by Count', fontsize=16)
plt.xlabel('Count')
plt.ylabel('Category')
plt.tight_layout()
plt.show()


import plotly.graph_objects as go
import os

# 读取CSV文件到DataFrame
csv_file_path = 'category_counts.csv'  # 替换为你的CSV文件路径
df = pd.read_csv(csv_file_path)

# 获取前50个出现次数最多的类别
top_50 = df.nlargest(50, 'Count').reset_index(drop=True)
top_50['Rank'] = range(1, len(top_50) + 1)

# 创建带有连线的散点图
fig = px.scatter(
    top_50,
    x='Rank',
    y='Count',
    text='Category',
    title='Top 50 Categories by Count with Connecting Lines',
    labels={'Rank': 'Rank', 'Count': 'Count'},
    color='Count',
    color_continuous_scale='Viridis'
)

# 添加自定义线条
fig.add_traces(
    go.Scatter(
        x=top_50['Rank'],
        y=top_50['Count'],
        mode='lines',  # 只显示线条
        line=dict(color='rgba(0, 0, 0, 0.5)', width=2),  # 设置线条颜色和宽度
        showlegend=False
    )
)

# 自定义样式
fig.update_traces(textposition='top center')
fig.update_layout(
    title_font_size=24,
    xaxis_title_font_size=18,
    yaxis_title_font_size=18,
    showlegend=False
)

# 指定输出文件路径
output_folder = os.getcwd()  # 当前工作目录
output_file = os.path.join(output_folder, "line_connected_scatter_plot_top_50_categories.html")
fig.show()
# 保存为HTML文件
fig.write_html(output_file)

print(f"图表已保存为 {output_file}")