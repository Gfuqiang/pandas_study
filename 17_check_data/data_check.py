import pandas as pd

"""
数据校验
将score不在0到100之间的数据找出
"""

def check_data(df):
    if not 0 <= df.Score < 100:
        print(f'#{df.ID}\tName:{df.Name} has is a invalid score {df.Score}')

df = pd.read_excel('./Students.xlsx')
df.apply(check_data, axis=1) # 轴的概念df 重上到下为0，左到右为1 一行一行校验axis给1
print(df)
