r,c,zr,zc = map(int,input().split())
for i in range(r):
    a = input()
    b = ''
    for j in range(zr):
        for k in range(c):
            b += a[k]*zc
        print(b)