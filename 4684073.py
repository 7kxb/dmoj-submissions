t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    b = []
    d = 0
    for i in range(n):
        b.append(int(a[i]))
        c = 1
        for j in range(len(b)):
            c *= b[j]
        if c > d:
            d = c
    print(d%998244353)