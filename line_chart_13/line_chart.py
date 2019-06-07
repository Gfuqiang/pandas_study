import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Orders.xlsx', index_col='Week')
print(df.head())
print(df.columns)

# df.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])    # 默认x轴为index列
df.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])    # area为叠加折线图
# df.plot.bar(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'], stacked=True)    # 柱状图显示每周的数据 折线图可以看出走势
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=8, fontweight='bold')
plt.xticks(df.index) # 默认生成的x轴 间隔单位太大 重新定义x轴的间隔单位  xticks方法对x轴进行操作
plt.show()