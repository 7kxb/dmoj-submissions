n = int(input())
c = 0
a = list(map(int,input().split()))
for i in range(n):
    if i == a[i]:
        c += 1 
print(c)