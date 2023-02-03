n = int(input())
for i in range(n):
    a = int(input())
    b = False
    for i in range(64):
        if a == 1.0:
            b = True
        else:
            a = a/2
    if b:
        print('T')
    else:
        print('F')