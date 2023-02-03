n,t = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a.pop(-1)
b = 0
for i in range(len(a)):
    b += a[i]
    if b > t:
        b -= a[i]
        pass
print(i)