n,s = map(int, input().split())
a = list(map(int, input().split()))
def buffet(n,s,a):
    c = a
    c.sort()
    if n <= s and c[0] == 2:
        return('INF')
    else:
        t = True
        b = 0
        while t:
            print(a)
            for i in a:
                if a[i] == 0:
                    return(b)
                else:
                    a[i] -= 1
            c = a
            c.sort()
            a[a.index(c[0])] += s
            b += 1
print(buffet(n,s,a))