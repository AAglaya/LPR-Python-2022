import numpy as np
import matplotlib.pyplot as plt

plt.ylabel("Ось Y в логарифмисечском масшатбе")
plt.xlabel("Ось X")
plt.yscale('log')
plt.grid(True)
x = np.linspace(0, 100, 100)
y = x**3
plt.plot(x, y, "k--")
plt.show()