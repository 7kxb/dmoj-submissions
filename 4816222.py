n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a < 4 or b < 4:
        print('bad')
    else:
        print('good')