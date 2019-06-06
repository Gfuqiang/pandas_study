import pandas as pd
import matplotlib.pyplot as plt

"""
柱状图
"""

df = pd.read_excel('./Students.xlsx')
df.sort_values(by='Number', inplace=True, ascending=False)           # 排序
print(df)
# ============ pandas 制图方法 ==========
# df.plot.bar(x='Field', y='Number', color='red', title='Student Number')      # pandas的绘图工具
# ===========使用 matplotlib========
plt.bar(df.Field, df.Number, color='orange')       # 传入数据
plt.xticks(df.Field, rotation='90') # 旋转field列字体90度
plt.xlabel('Field')     # 添加x轴名称
plt.ylabel('Number')            # 添加y轴名称
plt.title('International Student Field', fontsize=16)
plt.tight_layout()     # 将Field显示全
plt.show()