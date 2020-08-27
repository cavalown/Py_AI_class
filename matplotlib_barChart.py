import matplotlib.pyplot as plt
import numpy as np
X = np.arange(20) #從0~19的數值
Y = np.random.uniform(0.5,1.0, 20) #隨機產生20個範圍從0.5~1.0的數值
#長條圖上的數字
for x, y in zip(X, Y):
# ha: horizontal alignment 長條圖上面數字的對齊方式 (水平)
# va: vertical alignment長條圖上面數字的對齊方式 (垂直)
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom', fontsize=6)
# edgecolor長條圖邊框顏色, facecolor長條圖顏色
plt.bar(X,Y,facecolor='#9999ff', edgecolor='white')
plt.show()