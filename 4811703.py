k = int(input())
for i in range(k):
    n,m = map(int,input().split())
    print(2*min(n-1,m-1))