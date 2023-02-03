a = input()
i = 0
while i != len(a)-2:
    for i in range(1,len(a)):
        if a[i-1] == 'A' and a[i] == 'A':
            a = a[:i] + ' ' + a[i:]
            break
        if a[i-1] != 'A' and a[i] != 'A':
            a = a[:i] + ' ' + a[i:]
            break
print(a)