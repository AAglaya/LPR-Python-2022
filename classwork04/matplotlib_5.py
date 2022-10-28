import numpy as np
import matplotlib.pyplot as plt

plt.ylabel("Это ось Y")
plt.xlabel(r"Это ось X: $e^{-xsin(x)}$")
x = np.linspace(10, 100, 10000)
y = np.e**(-x*np.sin(x))
plt.plot(x, y)
plt.ylim(0, 10)
plt.grid()
plt.minorticks_on()
plt.show()