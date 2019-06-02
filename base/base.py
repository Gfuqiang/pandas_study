import pandas as pd
import random


# 使用series创建DataFrame
# data = {k: chr(random.randint(65, 90)) for k in range(4) for _ in range(4)}
# print(data)
# k is index, v is value

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], name='A')
s2 = pd.Series([i for i in range(5, 9)], index=['a', 'b', 'c', 'd'], name='B')
# s3 = pd.Series(data, name='C')
# print(s1)
# print(s2)

# 将series 组合为dataframe
# NaN not a number
df = pd.DataFrame({s1.name: s1, s2.name: s2})
df1 = pd.DataFrame(s1, s2)
# print(df)
print(df1)
