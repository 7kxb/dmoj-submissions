n,m = map(int,input().split())
p = list(map(int,input().split()))
a = list(map(int,input().split()))
b = 0
for i in range(n-1):
    c = 0
    for j in range(i,n-1):
        c += a[j]
        b += c
print(b)