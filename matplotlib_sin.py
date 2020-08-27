import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-np.pi,np.pi,200)
y = np.sin(x)
#原始的圖案
plt.plot(x,y)
plt.show()
#線條 顏色 寬度 樣式
plt.plot(x,y,color='blue',linewidth=1.0, linestyle='--')
#增加坐標軸長度
plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(y.min()*1.2, y.max()*1.2)
#座標刻度 (Latex語法)
plt.xticks((-np.pi,-np.pi/2,np.pi/2,np.pi),( r'$-\pi$',r'$-\pi/2$',r'$+\pi/2$',r'$+\pi$'))
plt.yticks([-1, -0.5, 0, 0.5, 1])
g = plt.gca() #取得GCA目前座標軸
g.spines['right'].set_color('none') #隱藏右框線
g.spines['top'].set_color('none') #隱藏上框線

g.xaxis.set_ticks_position('bottom') #設定x軸刻度顯示位置
g.spines['bottom'].set_position(('data',0))#移動設定x軸位置
g.yaxis.set_ticks_position('left') #設定y軸刻度顯示位置
g.spines['left'].set_position(('data',0)) #移動設定y軸位置
#標出特定的紅線
t = 3 * np.pi/4
plt.plot([t,t],[0,np.sin(t)],color='red',
linewidth=1.5,linestyle=':')
#標出特定的紅點
plt.scatter(t,np.sin(t), 20, color='red')
print(np.sin(t))
#設定紅點的說明 (Latex語法), frac代表分數
plt.annotate(r'$ sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2} $',xy=(t,np.sin(t)), xycoords='data',
xytext=(-90,-50), textcoords='offset points', fontsize='10',
arrowprops = dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
)
#設定坐標軸刻度文字
for label in g.get_xticklabels()+g.get_yticklabels():
    label.set_fontsize(8)
    label.set_color('purple')
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=.65))
plt.show()