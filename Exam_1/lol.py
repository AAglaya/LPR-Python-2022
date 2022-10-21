import numpy as np
from matplotlib import pyplot as plt


data2 = data.reshape(len(data)*2)
plt.hist(data2, "auto")
plt.savefig('histograms_0.jpg')

plt.show()