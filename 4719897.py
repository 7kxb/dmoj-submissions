def s():
    for i in range(2,n+1):
        if info[i]:
            j = 2
            while j*i < n+1:
                info[j] = False
                j + 1
def m(n,i,x):
    return i/x+1
def p(n,i,x):
    if i != n:
        return m(0,n-i,x) + m(0,n-i-1,x)
    return m(0,n-i,x)
n, x = map(int, input().split())
info = []
for i in range(n+1):
    info.append(True)
s()
ans = 0
for i in range(2,n+1):
    if info[i]:
        ans += p(n,i,x)
print(int(ans))