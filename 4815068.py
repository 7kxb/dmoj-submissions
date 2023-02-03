def grid(n,m,a):
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o' and a[i+1][j] == '.':
                a[i] = a[i][:j] + '.' + a[i][j+1:]
                a[i+1] = a[i+1][:j] + 'o' + a[i+1][j+1:]
    return a 
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(input())
a.append('x'*m)
for i in range(100):
    a = grid(n,m,a)
for i in range(n):
    print(a[i])