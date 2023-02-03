n,k,x = map(int,input().split())
if x%2==0:
    print(x%k,x%k)
else:
    print(x%k,x%k-1)