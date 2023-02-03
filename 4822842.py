n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(n):
    print(str(a[i]),end=' ')