import numpy as np

a = np.random.randint(1,20,16).reshape(4,4)
print('---a')
print(a)

b = np.sort(a, axis=0)  #同行排序小到大
print('---b')
print(b)

c = np.sort(b, axis=1)  #同列排序小到大
print('---c')
print(c)

np.save('c', c)   #存成二進為值(預設)，副檔名為 npy(容量較小)，這是預設值。
np.savetxt('c', c)  #存成文字檔(為了可讀性)

d = np.load('c.npy')
print('---d')
print(d)

e = np.loadtxt('c')
print('---e')
print(e)