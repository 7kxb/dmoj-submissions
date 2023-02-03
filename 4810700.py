n = int(input())
a = list(map(int,input().split()))
o = 0 
e = 0
for i in range(n):
    if a[i]%2 == 1:
        o += 1 
    else:
        e += 1 
print(o//2+e//2)