# -*- coding: utf-8-*-

from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

# 从 csv 文件读取抓取到的结果，指定第一行为各个列的名称
df = pd.read_csv('answers.csv', header=0)

# 以 author_name 列进行分组
gb = df.groupby('author_name').sum()['voteup_count']

# 对求和结果进行排序并取出前十
all_authors = gb.sort_values()
top_10_authors = all_authors[-13:-2]

print(top_10_authors)

# 加载中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 初始化图表绘图区域
plt.figure()

# 直接使用 pandas 提供的绘图接口绘图
top_10_authors.plot.barh()

# 显示绘制好的图标
plt.show()