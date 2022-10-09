b = set([str(i) for i in range(10)])
while True:
    a = input()
    if a.isdigit():
        b = b & set(a)
    else:
        break
print(b)