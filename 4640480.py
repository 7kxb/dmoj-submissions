n = int(input())
for i in range(n):
    a = input().split()
    if int(a[0]) < 1989:
        print('Yes')
    elif int(a[0]) == 1989:
        if int(a[1]) == 1:
            print('Yes')
        elif int(a[1]) == 2:
            if int(a[2]) <= 27:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')