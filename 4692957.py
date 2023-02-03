def d(e):
    f = [False, False] + [True] * (e-1)
    for i in range(2, e-1):
        if f[i] == True:
            for j in range(2*i, len(f), i):
                f[j] = False
    return f
for i in range(5):
    a = int(input())
    b = d(a)
    c = 0
    for i in range(a+1):
        if b[i] == True:
            c += i
    print(c)