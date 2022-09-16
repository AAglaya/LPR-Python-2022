win_9 = -1
win_10 = -1
win_11 = -1

with open("input.txt", "r", encoding='utf-8') as f:
    while True:
        a = f.readline().strip('\n')
        if not a:
            break
        a = list(a.split())
        grade = int(a[2])
        rez = int(a[3])
        if grade == 9 and rez >= win_9:
            win_9 = rez
        if grade == 10 and rez >= win_10:
            win_10 = rez
        if grade == 11 and rez >= win_11:
            win_11 = rez
            
print(win_9, win_10, win_11, sep=' ')