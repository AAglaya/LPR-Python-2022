import numpy as np

array = np.array([i for i in range(1, 100)])
array2 = np.array([sum(array[i:i+3]) for i in range(0, 99, 3)])