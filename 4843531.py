t = int(input())
for i in range(t):
    a,b,n = map(int,input().split())
    while t:
        c += b
        if c > n:
            c -= b
            c += a
            if c == n:
                t = False
                print('YES')
            elif c > n:
                t = False
                print('NO')