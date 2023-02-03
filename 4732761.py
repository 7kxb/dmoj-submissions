n = int(input())
s1 = []
f1 = []
for i in range(n):
    s2,f2 = map(int, input().split())
    s1.append(s2)
    f1.append(f2)
while True:
    s2,f2 = map(int, input().split())
    c = 0
    f = False
    if s2 == 0 and f2 == 0:
        break
    else:
        for i in range(n):
            if f1[s1.index(s2)] != f2:
                s2 = f1[s1.index(s2)]
                c += 1 
            else:
                print('Yes',c)
                f = True
                break 
    if not f:
        print('No')