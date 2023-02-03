n,m = map(int,input().split())
a = 1
b = 2
c = 1
for i in range(m):
    print(a,b)
    a += 1
    b += 1
    if b > m:
        a += 1
        b = a + 1
        if a > m:
            a = 1
            c += 1
            b = a + c