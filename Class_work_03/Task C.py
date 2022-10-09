a = list(map(set, input().split()))
b = a[0]
for i in range(len(a)):
    b = b & a[i]

print(b)