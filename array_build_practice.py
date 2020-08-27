import numpy as np

a = np.array([1, 2, 3])   #一維陣列
print(a)
print(a.ndim)  #查看維度
print(a.shape) #查看形狀
print(a.size) #查看大小
print(a.dtype) #查看資料型態

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

c = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)