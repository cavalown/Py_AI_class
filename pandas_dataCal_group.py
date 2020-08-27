import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,100,24).reshape(6,4),columns=list('ABCD'))

print('--1')
print(df)
print()

print('--2')
print(df.head(3))  # 取得前三列
print()

print('--3')
print(df.tail(2)) # 取得後二列
print()

print('--4')
# 基本運算 : 平均, 標準 差, 最小 ,中位數, 最大 ( 中位數是指將數據按大小順序排列起來，形成一個數列，居於數列中間位置的那個數據 )
print(df.describe())
print()

print('--5')
df['TAG'] = ['M','F','F','M','F','M']  # 加入 一 TAG 欄
print(df)
print()

print('--6')
# 設定浮點數顯示方式
pd.options.display.float_format = '{:,.0f}'.format
print(df.groupby('TAG').sum()) # 以 TAG 標籤 分組 總 和
print()

print('--7')
print(df.groupby('TAG').mean()) # TAG 標籤 分組平均
print('')