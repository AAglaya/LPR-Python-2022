with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: [y for y in x.rstrip().split()], a))

for i in range(len(a) - 1, -1, -1):
    print(*a[i])