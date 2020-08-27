import  numpy as np
a = np.arange(15).reshape(3,5)
print(a)
print('')
print(a.sum(axis=0)) #針對(同)行相加 print(‘’)
print(a.sum(axis=1)) #針對(同)列相加 print(‘’)
print(a.max(axis=0)) #針對(同)行取最大元素 print(‘’)
print(a.max(axis=1)) #針對(同)列取最大元素