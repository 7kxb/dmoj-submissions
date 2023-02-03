a = input()
b = input()
c = 0
for i in range(len(a)):
    if a[i] != b[i]:
        c += 1
if c == 1:
    print('LARRY IS SAVED!')
else:
    print('LARRY IS DEAD!')