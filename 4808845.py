r,c,zr,zc = map(int,input().split())
for i in range(r):
    a = input()
    for j in range(zr):
        b = ''
        for k in range(c):
            b += a[k]*zc
        print(b)