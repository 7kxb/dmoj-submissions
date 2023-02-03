a = input().split()
b = 1
for c in range(len(a)):
    if a[c] == 'not':
        b *= -1
    elif a[c] == 'False':
        b *= -1
if b == -1:
    print('False')
elif b == 1:
    print('True')