#Numpy二維陣列的索引
import numpy as np
a = np.arange(0,36).reshape(6,6)
print(a)
print('---')

print(a[4,5])
print(a[4,-1])
print('---')


print('*取第3列的第1欄到第4欄前停止')
print(a[3, 1:4])
print('*取從頭到第3列前停止，從第3欄到最後')
print(a[:3, 3:])
print('*取第2列的所有欄')
print(a[2,:])
print('*取每一列的第三欄')
print(a[:,3])  #理論上是行向量，但Numpy是列向量
print('*取所有列，以2等差取欄')
print(a[:, ::2])
print('*從頭以2等插取列，從頭以3等插取欄')
print(a[::2, ::3])