a = list(map(str,input().split()))
b = 0
for i in range(len(a)):
    b += len(a[i])
print(b)