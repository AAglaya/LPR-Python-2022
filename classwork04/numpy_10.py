import numpy as np


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def x_pow(x, n):
    if n == 1:
        return x
    else:
        return np.dot(x_pow(x, n-1), x)


k = int(input()) #степень, в которую надо возвести матрицу
n = int(input()) #размер матрицы
#x = np.random.randint(100, size=(n, n))      #<--- задать матрицу рандомно
x = np.array([[1, 2], [3, 4]])
x_i = np.eye(n)
shape = (n, n)
e = np.zeros(shape)

for i in range(0, k+1):
    if i == 0:
        e += x_i
    else:
        temp = x_pow(x, i)
        temp = temp / factorial(i)
        e += temp
print(e)




