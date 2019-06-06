import pandas as pd
import matplotlib.pyplot as plt

"""
双条或多条柱状图
"""

df = pd.read_excel('./Students.xlsx')
df.sort_values(by='2017', inplace=True, ascending=False) # 排序
print(df)

df.plot.bar(x='Field', y=['2016', '2017'], color=['red', 'green'])
plt.title('International Student field', fontsize=16, fontweight='bold')
plt.xlabel('Field', fontsize=13, fontweight='bold')
plt.ylabel('Number', fontweight='bold')

ax = plt.gca() # 获取x轴的操作
ax.set_xticklabels(df.Field, rotation='45', ha='right') # 对Field 旋转45度 ha表示水平旋转，没有这个参数以中心点旋转
af = plt.gcf() # 获取 figure（图形）
af.subplots_adjust(left=0.2, bottom=0.4) # 调整图形布局
plt.show()