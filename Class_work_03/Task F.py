a = {i : chr(i) for i in range(ord('a'), ord('z')+1)}
b = {v : (k - ord('a') + 1) for k, v in a.items()}
print(b)