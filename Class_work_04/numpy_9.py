import numpy as np


def prime_numbers(n):
    IsPrime = [1] * (n + 1)
    IsPrime[0], IsPrime[1] = 0, 0
    p = 2
    while p * p <= n:
        if IsPrime[p]:
            for i in range(p * p, n + 1, p):
                IsPrime[i] = 0
        p += 1
    numbers = [i for i in range(n+1) if IsPrime[i] == 1]
    return numbers


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n, m = 10, 30
prime = np.array([-i for i in prime_numbers(m)])
fib = np.array([fibonacci(i) for i in range(1, n+1)])
ans = np.dot(prime, fib)
print(ans)