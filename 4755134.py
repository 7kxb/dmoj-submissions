n = int(input())
a = list(map(int,input().split()))
e = 0
b = a[:n]
c = a[n:]
d = 0
for j in range(n):
    if b[j] == c[j]:
        d += 1
if d > e:
    e = d
print(e)