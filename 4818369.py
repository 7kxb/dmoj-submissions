f,n = map(int,input().split())
a = []
for i in range(f):
    a.append(int(input()))
a.sort()
b = 0
for i in range(1,n+1):
    b += (a[n-i]**i)
print(b)