n = int(input())
for _ in range(n):
    a = str(input())
    b = True
    for i in range(len(a)):
        if a[i] == 'k' or a[i] == 'n' or a[i] == 'm' or a[i] == 'r':
            if i != len(a)-1:
                if a[i+1] != 'a' and a[i+1] != 'e' and a[i+1] != 'i' and a[i+1] != 'o' and a[i+1] != 'u':
                    b = False
            else:
                b = False
        elif a[i] == 'h':
            if i != len(a)-1:
                if a[i+1] != 'a' and a[i+1] != 'e' and a[i+1] != 'i' and a[i+1] != 'o':
                    b = False
            else:
                b = False
        elif a[i] == 'f':
            if i != len(a)-1:
                if a[i+1] != 'u':
                    b = False
            else:
                b = False
        elif a[i] != 'a' and a[i] != 'e' and a[i] != 'i' and a[i] != 'o' and a[i] != 'u':
            b = False
    if b:
        print('YES')
    else:
        print('NO')