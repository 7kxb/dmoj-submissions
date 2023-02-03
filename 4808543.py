n,c = map(int,input().split())
a = list(map(int,input().split()))
b = []
c = []
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    c.append([b[i],a.count(b[i])])
c.sort(key=lambda z: z[1], reverse = True)
d = ''
for i in range(len(c)):
    d += (str(c[i][0]) + ' ')*c[i][1]
print(d)