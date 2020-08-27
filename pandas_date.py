import pandas as pd
import numpy as np
#建立ABC欄日期從20200101~20200105的資料,匯入到DataFrame
d = { 'A' : pd.Series(data=np.random.randint(10,30,5), index=pd.date_range('20200101',periods=5)),
      'B' : pd.Series(data=np.random.randint(50,80,5), index=pd.date_range('20200101',periods=5)),
      'C' : pd.Series(data=np.random.randint(100,150,5), index=pd.date_range('20200101',periods=5)) }
df = pd.DataFrame(d, index=pd.date_range('20200101',periods=5))

print('--1')
print(df)
print('')

print('--2')
df['D'] = df['B'] + df['C']  # 欄與欄進行 運算 , 結果產生新的 D 欄 , 附加上去
print(df)
print('')

print('--3')
print(df.loc['20200102':'20200104'])  # 按日期區間擷取
print('')

print('--4')
del df['A']  # 刪除 A 欄
print(df)
print('')

print('--5')
df['E'] = pd.Series(data=[10,20,30,40,50], index=pd.date_range('20200101',periods=5)) # 增加 E 欄
print(df)
print('')

print('--6')
print(df['B'].values)  # B 欄的值
print('')

print('--7')
print(df.T) # 轉置
print('')

print('--8')
df = df.drop(pd.to_datetime('20200101')) # 刪除 row index = 20200101
print(df)
print('')

print('--9')
df = df.drop(pd.date_range('20200103',periods=2))  # 刪除 2 列
print(df)
print('')

print('--10')
d = { 'B': 10, 'C': 20, 'D': 30, 'E': 40, }  # 增加 1 列
df = df.append(pd.DataFrame(data=d ,index=pd.date_range('20200106',periods=1)), sort=True)
d = [{ 'B': 11, 'C': 21, 'D': 31, 'E': 41, }, { 'B': 32, 'C': 22, 'D': 32, 'E': 42, }]    # 增加 2 列
df = df.append(pd.DataFrame(data=d ,index=pd.date_range('20200107',periods=2)), sort=True)
print(df)
print('')