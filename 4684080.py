t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    d = 0
    for i in range(n):
        c = 1
        for j in range(len(a)):
            c *= int(a[j])
            if c > d:
                d = c
    print(d%998244353)