import pandas as pd

"""
使用sum 和 mean（平均）函数对一列进行求和 平均数
"""

df = pd.read_excel('./Students.xlsx', index_col='ID')
test_df = df[['Test_1', 'Test_2', 'Test_3']]           # 取出指定的列
df_sum = test_df.sum(axis=1)              # axis是轴的概念，1（从左到右）为一行一行计算 0 （从上到下）  一列一列计算
df_mean = test_df.mean(axis=1)
# print(df_sum)
# print(df_mean)
df['sum'] = df_sum
df['mean'] = df_mean
print(df)
student_table = df[['Test_1', 'Test_2', 'Test_3', 'sum', 'mean']].mean()
student_table['Name'] = 'Students'
student_table = df.append(student_table, ignore_index=True)      # append 函数会将一个series当做一行添加到dataframe中
print(student_table)