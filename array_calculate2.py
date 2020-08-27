import numpy as np

a = np.arange(6).reshape(3,2)
print('---a')
print(a)

b = np.arange(6).reshape(2,3)
print('---b')
print(b)

c = np.dot(a,b)  #矩陣內積
print('---c')
print(c)

d = np.matmul(a,b)  #矩陣內積
print('---d')
print(d)

print('---轉至矩陣c')
print(c.T)
