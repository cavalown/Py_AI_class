import numpy as np

a = np.array([[1,2,3,4],[4,5,6,7]])
b = np.random.randint(1,3,8).reshape(2,4)

print('---a')
print(a)
print('---b')
print(b)  #形狀一樣
print('---a*b')
print(a*b)
print()

c = np.array([1,2]).reshape(2,1)  #乘法廣播
print('---c')
print(c)
print('---a*c')
print(a*c)
print()

d = np.array([1,1,1,1])
print('---a+b')
print(a+d)

e = np.array([1,2]).reshape(1,2)  #乘法廣播
print('---e')
print(e)
print('---a*e')
print(a*e)
#ValueError: operands could not be broadcast together with shapes (2,4) (1,2)
