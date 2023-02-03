n = int(input())
m = int(input())
k = int(input())
a = [[0 for i in range(m)]for i in range(n)]
b = 0
for i in range(k):
    c,d = input().split()
    if c == 'R':
        for j in range(m):
            a[int(d)-1][j] += 1
            if a[int(d)-1][j]%2 == 0:
                b -= 1
            else:
                b += 1
    if c == 'C':
        for k in range(n):
            a[k][int(d)-1] += 1
            if a[k][int(d)-1]%2 == 0:
                b -= 1
            else:
                b += 1
print(b)