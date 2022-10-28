import numpy as np
import matplotlib.pyplot as plt

plt.ylabel("Это ось Y")
plt.xlabel(r"Это ось X $sin(x) x^{-2}$")
x = np.linspace(0, 100, 10)
y = np.sin(x)*x**(-2)
plt.plot(x,y)
plt.grid()
plt.show()