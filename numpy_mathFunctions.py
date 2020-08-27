import numpy as np

a = np.arange(6)
b = np.array([0,1,2,3,4])
c = np.array([6,1,1,1,1])

print('---a')
print(a)
print('sum of a')
print(a.sum())
print('mean of a,b,c')
print(a.mean(), b.mean(), c.mean())

#Std()標準差: 一個較大的標準差，代表大部分的數值和其平均值之間差異較大；
# 一個較小的標準差，代表這些數值較接近平均值。
print('---standard deviation')
print(a.std(), b.std(), c.std())
print('---min of a')
print(a.min())
print('---max of a')
print(a.max())