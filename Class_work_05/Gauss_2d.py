import numpy as np
import matplotlib.pyplot as plt


mu, sigma = 0, 1
np.random.seed(0)
data_x = np.random.normal(mu, sigma, 100000)
data_y = np.random.normal(mu, sigma, 100000)

hist, x_edges, y_edges = np.histogram2d(data_x, data_y, bins=(50, 50))
cs = plt.matshow(hist)
plt.colorbar(cs)

plt.show()