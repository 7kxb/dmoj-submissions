n = int(input())
a = list(map(int,input().split()))
e = 0
for i in range(n*2):
    if i < n:
        b = a[i:n+i]
        c = a[n+i:] + a[:i]
    else:
        b = a[i:n+i] + a[:i%n]
        c = a[i%n:n+i%n]
    d = 0
    for j in range(n):
        if b[j] == c[j]:
            d += 1
    if d > e:
        e = d
print(e)