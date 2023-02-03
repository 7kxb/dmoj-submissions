n = int(input())
for i in range(n):
    p,c = map(float,input().split())
    print(p/(1+c/100))