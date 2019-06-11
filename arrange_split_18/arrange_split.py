import pandas as pd

"""
列的拆分 （合并）
将一列进行拆分
"""

df = pd.read_excel('./Employees.xlsx', index_col='ID')
df1 = df['Full Name'].str.split(' ', expand=True, n=1)    # expand参数表示直接将一列拆分而不是表示为一个列表 第一个参数表示以什么字符串进行切分 n表示保留切分后保留的个数
"""
可以查找str还有很多方法：查询Series.str 找pandas文档
"""
df['First Name'] = df1[0]
df['Last Name'] = df1[1]
print(df)
print(df1)