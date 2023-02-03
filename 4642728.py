n = int(input())
a = input().split()
b = input().split()
c = []
d = []
t = True
for i in range(n):
    c.append(a[i])
    d.append(b[i])
    a[i] == '0'
    b[i] == '0'
    e = b.index(c[i])
    f = a.index(d[i])
    if e != f:
        print('bad')
        t = False
        break
    elif c[i] == d[i]:
        print('bad')
        t = False
        break
if t:
    print('good')