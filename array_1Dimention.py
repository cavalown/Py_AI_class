import numpy as np

a = np.arange(6)
print(a)

print(a[2])  #索引 2
print(a[3:5])  #從3開始到5停止
print(a[2:-1])  #從2開始到-1停止
print(a[::1])  #1的倍數取等差
print(a[::-1])
print(a[::2])
print(a[::-2])  #2的倍數，從尾端取等差


a[2] = 0  #設定第二個位置的值=0
print(a)

a[3:5] = 0
print(a)
print(a[3:5])
print(a[1:])