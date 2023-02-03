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
                if a[i+1][j-1] == '#' and a[i+1][j] == '#' and a[i+1][j+1] == '#':
                    c += 1
                if a[i+1][j-1] == '#' and a[i+1][j] == '#' and a[i+1][j+1] == '#' and a[i+2][j-2] == '#' and a[i+2][j-1] == '#' and a[i+2][j] == '#' and a[i+2][j+1] == '#' and a[i+2][j+2] == '#':
                    c += 1
    print(c)