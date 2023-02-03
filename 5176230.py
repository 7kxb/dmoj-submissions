n, m = map(int,input().split())
a = n*m
if a % 2 == 0:
    print(min(n,m)*(max(n,m)//2),min(n,m)*(max(n,m)//2))
else:
    print(min(n,m)*(max(n,m)//2+1),min(n,m)*(max(n,m)//2))