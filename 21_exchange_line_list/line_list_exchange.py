import pandas as pd

"""
列和行进行翻转
"""

pd.options.display.max_columns = 999 # 显示所有的列
df = pd.read_excel('./Videos.xlsx', index_col='Month')
table = df.transpose()  # 进行翻转
print(table)