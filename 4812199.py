a = list(map(int,input().split()))
b = 0
for i in range(8):
    if a[i] == i+1:
        b += 1
    if a[i] == 8-i:
        b -= 1
if b == 8:
    print('ascending')
elif b == -8:
    print('descending')
else:
    print('mixed')