import pandas as pd
from datetime import datetime

"""
1. 自动填充数据
2. 从有数据的位置开始读取 (数据的位置不是在第一格，是在表的某一位置)
"""

df = pd.read_excel('./a.xlsx', skiprows=3, usecols='B:E', index_col=None,     # skiprows 重第几行开始读数据，  usecols 获取哪几列
                   dtype={'id': str, 'name': str, 'data': str, 'date': str})    # nan行默认是float64类型 dtype指定为str

date_time = datetime.now()
for i in df.index:
    # print(pd)
    df['id'].at[i] = i + 1
    df['data'].at[i] = 'YES' if i % 2 == 0 else 'NO'
    df['date'].at[i] = date_time


print(type(df['id']))   # df['id'] 获取的是Series
print(type(df.at[1, 'id']))     # 一行一行的读取
df.set_index('id', inplace=True)    # 设置id列为索引
print(df)
