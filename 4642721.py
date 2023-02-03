n = int(input())
a = input().split()
b = input().split()
c = []
d = []
t = True
for i in range(n):
    c.append(a[i])
    d.append(b[i])
    e = a.index(c[i])
    f = b.index(d[i])
    if e != f:
        print('bad')
        t = False
        break
    elif a[i] == b[i]:
        print('bad')
        t = False
        break
if t:
    print('good')