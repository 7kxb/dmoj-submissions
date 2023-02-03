n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append(int(a[i]))
b.sort()
c = -1
d = 1
e = []
for i in range(n):
    if c == b[i]:
        d += 1
        e.append((c,d))
    else:
        d = 1
    c = b[i]
f = b[-1]
for i in range(len(e)):
    if e[i][0]*e[i][1] > f:
        f = e[i][0]
print(f)