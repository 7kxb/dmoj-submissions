a = list(map(int,input().split()))
if a[0]-1 == a[1]:
    print('ascending')
elif a[0]+1 == a[1]:
    print('descending')
else:
    print('mixed')