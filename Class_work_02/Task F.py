n, t, e = -1, -1, -1
with open("input.txt", "r", encoding='utf-8') as f:
	while True:
		a = list(f.readline().strip('\n').split())
		if not a:
			break
		if int(a[2]) == 9:
			if int(a[3]) >= n:
				n = int(a[3])
		if int(a[2]) == 10:
			if int(a[3]) >= t:
				t = int(a[3])
		if int(a[2]) == 11:
			if int(a[3]) >= e:
				e = int(a[3])
print(n, t, e, sep = ' ')