a = {i : chr(i) for i in range(ord('a'), ord('z')+1)}
b = {v : (k - ord('a') + 1) for k, v in a.items()}

word = input()
letters = set(word)
ans = 0

for i in letters:
    ans += b[i]

print(ans)