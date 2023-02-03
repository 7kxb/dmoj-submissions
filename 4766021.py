a = list(map(str, input().split()))
b = int(a[0])
for i in range(len(a)):
    if a[i] == 'P':
        b += int(a[i+1])
    if a[i] == 'M':
        b -= int(a[i+1])
print(b)