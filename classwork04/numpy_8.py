import numpy as np

array = np.array([i for i in range(1, 100)])
array2 = np.array([sum(array[i:i+3]) for i in range(0, 99, 3)])
matrix = array2.reshape(11, 3)
matrix2 = matrix[2:9:3]
print(matrix2)
det = np.linalg.det(matrix2)
print(det)

