t = int(input())
for i in range(t):
    k = int(input())
    a = 1
    while a != 0:
        if '888 ' in str((k+a)**3)+' ':
            print(k+a)
            a = 0
        else:
            a += 1