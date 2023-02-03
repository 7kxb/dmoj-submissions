for _ in range(5):
    n = int(input())
    a = []
    c = 0
    for i in range(n):
        b = input()
        a.append(b+'.')
    a.append('.'*n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == '#':
                c += 1
                for k in range(1,n+1):
                    z = k*2+1
                    if a[i+k][j-k:j+k+1] == '#'*z:
                        c += 1
                    else:
                        break
    print(c)