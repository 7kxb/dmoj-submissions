a = input().split()
c = []
for i in range(int(a[1])):
    b = input().split()
    if int(b[0]) == 1:
        if str(b[2]) in c:
            print('1')
        else:
            print('0')
    if int(b[0]) == 2:
        c.append(str(b[2]))