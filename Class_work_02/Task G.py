win = -1
win_school = [-1]

with open("input.txt", "r", encoding='utf-8') as f:
    while True:
        a = f.readline().strip('\n')
        if not a:
            break
        a = list(a.split())
        school = int(a[2])
        rez = int(a[3])
        if rez > win:
            win_school.pop()
            win_school.append(school)
            win = rez
        elif rez == win:
            win_school.append(school)

li = []
[li.append(x) for x in win_school if x not in li]

print(li)