n,m = map(int, input().split())
a = []
b = 0
for i in range(n):
    a.append(input()+'.')
a.append('.'*(m+1))
for j in range(n):
    for k in range(m):
        if a[j][k] == '*' and a[j][k+1] == '.' and a[j+1][k] == '.':
            b += 1
print(b)