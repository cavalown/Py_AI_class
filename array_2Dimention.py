import numpy as np

a = np.array([[11,12,13], [23,24,25], [34,35,36]])
#二維陣列
print(a)
print('---')


print(a[1])
print()
print(a[1:])
print()
print(a[1][1:])
print('---')


print(a[...,1])  #...代表省略列，取出第一行(列,行)
print()
print(a[1,...])  #取出第一列，省略行
print()
print(a[...,1:])  #...省略列，取出第一行所有元素