t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    l = [[a+b, c+d], [a+c, b+d], [a+d, b+c], [b+c, a+d], [b+d, a+c], [c+d, a+b]]
    for i in range(6):
        for j in range(6):
            if l[i] == l[j] and i != j:
                l[j] = 0
    for i in range(6):
        if 0 in l:
            m = l.index(0)
            l.pop(m)
    print(len(l))
    for i in range(len(l)):
        print(l[i][0], l[i][1])