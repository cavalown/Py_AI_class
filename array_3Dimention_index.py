#NumPy 三維陣列的索引
import numpy as np

a = np.arange(16).reshape(2,2,4)
print(a)
print('---')

print(a[0])  #取第0個二維陣列
print()
print(a[0,:,1:3])
print()
print(a[0,1,:-1])
print()
print(a[0:1])
print()
print(a[0][1]) #切片擷取
print()
print(a[0,1,2]) #陣列索引，取第0個二維陣列，裡面的第1列，裡面的第2欄
print()
print(a[0][1][2]) #切片擷取