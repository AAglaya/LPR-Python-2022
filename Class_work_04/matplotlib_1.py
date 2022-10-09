import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10)
y = np.sin(x)*x**(-2)
plt.scatter(x,y)
#plt.plot(x,y)
plt.show()