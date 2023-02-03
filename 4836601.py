d = int(input())
for i in range(d):
    t = int(input())
    if t == 0:
        print('Weekend')
    else:
        a = 0
        for j in range(t):
            a += int(input())
        print('Day',str(i+1)+':',str(a))