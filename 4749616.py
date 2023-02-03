t,m = map(int,input().split())
d = []
for i in range(t):
    x,c = map(str,input().split())
    if c == 'in':
        d.append(x)
    if c == 'out':
        if d[0] == x and m >= 1:
            d.pop(0)
            m -= 1
for i in d:
    print(i)