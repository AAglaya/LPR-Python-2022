sum_9, sum_10, sum_11 = 0, 0, 0
cnt_9, cnt_10, cnt_11 = 0, 0 , 0

with open("input.txt", "r", encoding='utf-8') as f:
    while True:
        a = f.readline().strip('\n')
        if not a:
            break
        a = list(a.split())
        grade = int(a[2])
        rez = int(a[3])
        if grade == 9:
            cnt_9 += 1
            sum_9 += rez
        if grade == 10:
            cnt_10 += 1
            sum_10 += rez
        if grade == 11:
            cnt_11 += 1
            sum_11 += rez

print(sum_9/cnt_9, sum_10/cnt_10, sum_11/cnt_11, sep=' ')