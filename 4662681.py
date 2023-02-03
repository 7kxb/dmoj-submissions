a = input().split()
for i in range(len(a)):
    if a[i][0].isupper:
        a[i] += '.'
b = ''
for i in range(len(a)):
    b += a[i] + ' '
print(b)