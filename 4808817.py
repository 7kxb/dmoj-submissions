n,w,h = map(int,input().split())
for i in range(n):
    a = int(input())
    if w**2+h**2 >= a**2:
        print('DA')
    else:
        print('NE')