n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
d = []
for i in range(1,k+2):
    d.append(i)
for i in range(n+1):
    for i in range(len(b)):
        if b[i] in a:
            c.append(d[i])
            d[i] = -1
            a[a.index(b[i])] = -1
    for i in range(len(b)):
        b[i] += 1 
        if b[i] == n+1:
            b[i] = 1
print(d)