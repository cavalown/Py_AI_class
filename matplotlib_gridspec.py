import matplotlib.pyplot as plt
import matplotlib.gridspec as grd
import numpy as np
x = np.linspace(-np.pi,np.pi,200)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.tanh(x)
y4 = np.exp(x)
plt.figure(figsize=(18,4))
G = grd.GridSpec(2,3) #2列3欄
axes1 = plt.subplot(G[0,:]) #0列全部欄
plt.plot(x,y1)
axes2 = plt.subplot(G[1,0]) #1列0欄
plt.plot(x,y2)
axes2 = plt.subplot(G[1,1]) #1列1欄
plt.plot(x,y3)
axes2 = plt.subplot(G[1,2]) #1列2欄
plt.plot(x,y4)
plt.show()
