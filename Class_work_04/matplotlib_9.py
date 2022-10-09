import numpy as np
import matplotlib.pyplot as plt

plt.ylabel("Ось Y в логарифмисечском масшатбе")
plt.xlabel("Ось X")
plt.yscale('log')
x = np.linspace(0, 100, 100)
y = x**3
plt.plot(x, y, "k--", label="Пунктирная линия")
plt.grid()
plt.legend()
plt.show()