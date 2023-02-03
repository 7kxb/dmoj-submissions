n = int(input())
k = int(input())
m = input().split()
l = []
s = ''
for i in range(n):
    l.append((int(m[i]),int(m[i])%k))
l.sort(key=lambda y: y[0])
l.sort(key=lambda y: y[1])
for i in range(n):
    s += str(l[i][0]) + ' '
print(s)