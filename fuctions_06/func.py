import pandas as pd

df = pd.read_excel('./Books.xlsx')
"""
    ID      Name  ListPrice  Discount  Price
0    1  Book_001         10       0.5    NaN
1    2  Book_002         20       0.5    NaN
2    3  Book_003         30       0.5    NaN
3    4  Book_004         40       0.5    NaN
4    5  Book_005         50       0.5    NaN
5    6  Book_006         60       0.5    NaN
6    7  Book_007         70       0.5    NaN
7    8  Book_008         80       0.5    NaN

"""
print(df)
df.Price = df.ListPrice * df.Discount  # 计算price列的值
df.ListPrice = df.ListPrice * 10
print(df)
