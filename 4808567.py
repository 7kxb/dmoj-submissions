n,k = map(int,input().split())
p = list(map(int,input().split()))
a = 'YES'
for i in range(n):
    if p[i] == i%2:
        pass
    else:
        a = 'NO'
if a == 'NO':
    for i in range(n):
        if p[i] == i+1%2:
            pass
        else:
            a = 'NO'
print(a)