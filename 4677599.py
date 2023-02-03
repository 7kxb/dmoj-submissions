# i know this will WA, im just saving my code lol
n, m = map(int, input().split())
z = []
for i in range(n):
    a = input().split()
    for i in range(m):
        a[i] = int(a[i])
    z.append(a)
c = 50
d = [1,1]
for i in range(1,n-1):
    for j in range(1,m-1):
        b = z[i][j]
        if z[i-1][j] <= b or z[i][j-1] <= b:
            if z[i-1][j] <= z[i][j-1] and z[i-1][j] < c:
                c = z[i-1][j]-1
                d = [i-1, j]
            elif z[i][j-1] <= z[i-1][j] and z[i][j-1] < c:
                c = z[i][j-1]-1
                d = [i, j-1]
print(c)
# i know this will WA, im just saving my code lol