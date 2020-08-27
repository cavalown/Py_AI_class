import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
# 設定視角0.5
fig = plt.figure(figsize=plt.figaspect(0.5))
#第一個子圖
ax = fig.add_subplot(1, 2, 1, projection='3d')
X = np.arange(-6, 6, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y) #用座標點畫出格線
R = np.sqrt(X**2 + Y**2) #平方根
Z = np.sin(R)
#畫出surface表面圖, rstride, cstride跨度越大,格線間距越大
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.rainbow, linewidth=0, antialiased=False)
#z軸範圍設定
ax.set_zlim(-1.01, 1.01)
#設定顏色註解, shrink 影響長度, aspect 影響寬度
fig.colorbar(surf, shrink=0.5, aspect=10)

#第二個子圖
ax = fig.add_subplot(1, 2, 2, projection='3d')
X, Y, Z = get_test_data(0.1) #產生測試數據
#畫出線框圖
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0, antialiased=False)
#fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
