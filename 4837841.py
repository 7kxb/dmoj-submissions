n = int(input())
for i in range(1,n+1):
    a,b = map(int,input().split())
    if i == 1 or i == 2 or i == 6 or i == 20 or i == 70 or i == 252 or i == 924 or i == 3432 or i == 12870 or i == 48620 or i == 184756 or i == 705432:
        print(a-b)
    else:
        print(a+b)