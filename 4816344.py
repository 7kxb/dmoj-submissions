n,m = map(int,input().split())
p = list(map(int,input().split()))
a = list(map(int,input().split()))
b = 0
for i in range(n-1):
    c = 0
    for j in range(i,n-1):
        c += a[j]
        if i+1 <= p[0] and j+1 == p[1]-1:
            c -= sum(a[p[0]-1:p[1]-1])
        b += c
print(b%1000000007)