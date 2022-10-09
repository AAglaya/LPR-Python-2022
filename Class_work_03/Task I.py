s = input()
length = len(s)
s = s.replace(' ','')

for i in range(10):
  s = s.replace(str(i),'')

d = dict()

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in d:
  d[i] = d[i] / length

print(d)