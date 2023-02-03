n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a < 7 and b == 1:
        print('bad')
    elif a < 4 and b < 4:
        print('bad')
    elif a == 1 and b > 3:
        print('bad')
    else:
        print('good')