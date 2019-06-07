import pandas as pd
import matplotlib.pyplot as plt

"""
饼图
"""

df = pd.read_excel('./Students.xlsx', index_col='From')  # index指定饼图显示的内容名称
print(df)
df['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270) # counterclock 控制顺时针还是逆时针排  startangle： 12点钟位置开始作图
plt.title('Sources os International Student', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontweight='bold')
plt.show()