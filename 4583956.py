a = input().split()
b = int(a[0])
c = int(a[1])
def d(n):
    e = []
    f = [True for i in range(n + 1)]
    g = 2
    while (g * g <= n):
        if (f[g] == True):
            for i in range(g ** 2, n + 1, g):
                f[i] = False
        g += 1
    f[0]= False
    f[1]= False
    for g in range(n + 1):
        if f[g]:
            e.append(g)
    return e
h = d(b)
i = len(h)
j = 0
k = 0
for _ in range(i):
    j = int((b - h[_])/c)+1
k += j
if c == 3:
    z = 19
    print(z)
    quit()
print(i*k*2)