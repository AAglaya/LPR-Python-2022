import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(1, 100)])
y = np.array([np.e**(i*np.sin(i)) for i in x])
plt.ylim(0, 6)
plt.scatter(x, y)
plt.show()