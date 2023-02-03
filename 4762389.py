n,k = map(int, input().split())
a = list(map(int, input().split())) 
p = 0
d = 0
def lodge(n,k,a,p,d):
    for i in range(k):
            if p+k-i <= n-i and a[p+k-i] == 1:
                p += k-i
                return(p)
    p = -1
    return(p)
while p != n-1:
    p += lodge(n,k,a,p,d)
    if p != n-1:
        d += 1
    if p <= 0:
        print(-1)
        break
if p <= 0:
    pass
else:
    print(d)