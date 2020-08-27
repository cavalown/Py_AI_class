import numpy as np

a = np.arange(7)
print(a)

b = a[2:6]
print(b)

c = a[2:6].copy()  #copy
print(np.may_share_memory(a,b))
print(np.may_share_memory(a,c))

b[0] = 20

print(a)  #改變b，結果a也跟著改變了

print(c)  #改變b,結果c並不改變