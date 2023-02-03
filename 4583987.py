n = int(input())
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
            if g > n-20:
                e.append(g)
    return e
print(d(n+20)[0])