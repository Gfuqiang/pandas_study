import pandas as pd

"""
制定列进行排序
！！！注意  排序by 使用列表进行制定 使用两个sort_values 后边的一个会覆盖前边的
"""

df = pd.read_excel('./007.xlsx')
df.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=[False, False])        # by排序的字段， inplace不生成新的DataFrame, ascending False为倒叙
print(df)
