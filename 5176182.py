n, m = map(int,input().split())
a = n*m
if a % 2 == 0:
    print(a//2,a//2)
else:
    print(a//2+1,a//2)