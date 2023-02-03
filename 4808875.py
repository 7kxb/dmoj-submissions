a = input()
b = True
while b:
    for i in range(1,len(a)):
        if a[i-1] == 'A' and a[i] == 'A':
            a = a[:i]+' '+a[i:]
            c = False
            break
        elif a[i-1] != 'A' and a[i] != 'A':
            a = a[:i]+' '+a[i:]
            c = False
            break
        else:
            c = True
    if c:
        b = False
print(a)