import pandas as pd
import matplotlib.pyplot as plt

"""
叠加柱状图
"""

df = pd.read_excel('./Users.xlsx', index_col='ID')
df['num'] = df.Oct + df.Nov + df.Dec
# df['num'] = df['Oct'] + df['Nov'] + df['Dec']
df.sort_values(by='num', inplace=True)
print(df)
# df.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True)
df.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='Superposition chart') # barh方法是将x和y轴进行反转  stacked将多条柱状图进行叠加
plt.show()