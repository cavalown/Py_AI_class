import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 200)
plt.plot(x, x, label='linear') #直線
plt.plot(x, x**2, label='quadratic') #二次方
plt.plot(x, x**3, label='cubic') #三次方
plt.plot(x, np.exp(x), label='exponential') #指數
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
#plt.legend(loc='upper center')
plt.legend(loc='best')
plt.show()