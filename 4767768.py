n = int(input())
for i in range(n):
    a = int(input())
    b = False
    for i in range(32):
        if a == 1:
            b = True
        elif a == 2.0:
            b = True
        else:
            a = a/2
    if b:
        print('T')
    else:
        print('F')