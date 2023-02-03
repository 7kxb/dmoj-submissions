n,k,x = map(int,input().split())
if k%2==0 and x%2==0:
    print(x%k,x%k)
elif k%2==0 and x%2==1:
    print(x%k,x%k-1)
elif k%2==1 and x%2==0:
    print(x%k-1,x%k-1)
elif k%2==1 and x%2==1:
    print(x%k,x%k)