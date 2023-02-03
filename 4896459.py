t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] == 0:
            if a[i-2] > a[i-1]:
                a[i] = 10**9
            if a[i-2] < a[i-1]:
                a[i] = -1
    print(a)
    c = 0
    for i in range(1,n):
        if i%2 == 0:
            if a[i-1] > a[i]:
                c += 1
            else:
                c -= 1
        else:
            if a[i-1] < a[i]:
                c += 1
            else:
                c -= 1
    if c != n-1:
        for i in range(1,n):
            if i%2 == 0:
                if a[i-1] < a[i]:
                    c += 1
                else:
                    c -= 1
            else:
                if a[i-1] > a[i]:
                    c += 1
                else:
                    c -= 1
    if c == n-1:
        print('YES')
    else:
        print('NO')