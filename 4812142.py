a,b = map(int,input().split())
c,d = map(int,input().split())
e = a/c+b/d
g = 0
for i in range(1,4):
    f = a
    a = c
    f = b
    b = f
    c = d
    d = f
    if a/c+b/d > e:
        e = a/c+b/d
        g = i
print(g)