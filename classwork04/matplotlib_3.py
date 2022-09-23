import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10, 100, 10000)
y = np.e**(-x*np.sin(x))
plt.plot(x, y)
plt.ylim(0, 10)
plt.show()