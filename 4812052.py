n = int(input())
for i in range(56):
    a = list(map(float,input().split()))
    b = str(sum(a))[2]
for i in range(2,n+2):
    print(int(b)%i)