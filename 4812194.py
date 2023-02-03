a = list(map(int,input().split()))
b = 0
for i in range(1,9):
    if a[i] == i:
        b += 1
if b == 8:
    print('ascending')
b = 0
for i in range(8,0,-1):
    if a[i] == i:
        b += 1
if b == 8:
    print('descending')
else:
    print('mixed')