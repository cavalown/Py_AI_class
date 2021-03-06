import pandas as pd
import numpy as np

print('--1')
#隨機產生24個數值介於1~100之間
df = pd.DataFrame(np.random.randint(1,100,24).reshape(6,4),columns=list('ABCD'))
print(df)
print('')

print('--2')
print(df[3:5]) # 切出第 3 列到第 4 列, 若使用 df.loc[3:5],會 切 出第 3 列到 第 5 列
print('')

print('--3')
print(df[['A','B','D']]) #注意多個行的切片要使用兩個中括號
print('')

print('--4')
print(df.loc[3,'B'])  #(3,B) 元素
print('')

print('--5')
print(df.iloc[3,1]) # (3,1) 元素
print('')

print('--6')
print(df.iloc[2:5,0:2]) # 範圍 擷取
print()

print('--7')
print(df.loc[2:5,['A','B']]) # 範圍擷取
print()

print('--8')
print(df[df > 18])  # 篩選條件
print()

print('--9')
df[df > 18] = 100
print(df)
print('')

print('--10')
print(df[df.C > 50]) # 挑選 C 欄內符合條件的一整列
print('')