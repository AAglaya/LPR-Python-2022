m = int(input())
l = set(list(map(int, input().split())))
s = []

for i in l:
    if m - i in l and m - i != i and i not in s:
        print(i, m - i)
        s.append(i)
        s.append(m - i)