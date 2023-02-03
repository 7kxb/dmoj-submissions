t = int(input())
for i in range(t):
    a,b,n = map(int,input().split())
    c = 0
    d = True
    while d:
        c += b
        if c > n:
            c -= b
            c += a
            if c == n:
                d = False
                print('YES')
            elif c > n:
                d = False
                print('NO')