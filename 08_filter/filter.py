import pandas as pd
"""
按条件进行过滤
"""


def filter_age(a):
    return 20 <= a < 30


df = pd.read_excel('./Students.xlsx', index_col='ID')
s_df = df.loc[df['Age'].apply(lambda a: 20 <= a < 30)].loc[df.Score.apply(lambda s: 90 < s)]    # loc定位函数 location的缩写
# df['Age']， df.Age 语法相同都是在获取Series
# apply 在Series上执行函数
print(s_df)
print(df)
