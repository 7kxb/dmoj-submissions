n,k = map(int,input().split())
a = input()
c = 0
for i in range(len(a)):
    if a[i] == 'U':
        if k > 0:
            k -= 1
        if k == 0:
            c += 1
    elif a[i] == 'D':
        k += 1
    elif a[i] == 'F' and k == 0:
        c += 1
print(c)