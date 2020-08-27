import numpy as np

x = np.arange(25).reshape(5,5)
print(x)
print('---')

#跳躍式取值，抓取陣列特定元素
print(x[[0,1,2],[0,1,0]])
print('---')
#跳躍式取值，抓取第0列裡的特定元素(0,1) (0,2) (0,4)
print(x[[0],[1,2,4]])
print('---')
print(x[2,4])
print()
print(x[[2,4]])
print()
print(x[x>20]) #boolean index
print(x[x%2 == 0]) #boolean index

