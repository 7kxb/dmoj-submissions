n,a,b = map(int,input().split())
j = 0
k = 0
for i in range(n):
    x,y = map(int,input().split())
    if a > x:
        j += 1
    else:
        j += 2 
    if b > y:
        k += 1 
    else:
        k += 2
if j < k:
    print('Andrew wins!')
elif k < j:
    print('Tommy wins!')
else:
    print('Tie!')