for _ in range(5):
    n = int(input())
    m = int(input())
    x = []
    for i in range(m):
        a, b = map(int, input().split())
        if a*101 in x:
            x.append(a*101)
        elif a not in x:
            x.append(a)
        else:
            x.pop(x.index(a))
            x.append(a*101)
        if b*101 in x:
            x.append(b*101)
        elif b not in x:
            x.append(b)
        else:
            x.pop(x.index(b))
            x.append(b*101)
    c = 0
    for i in range(len(x)):
        if x[i] <= 100:
            c += 1
    print(c)