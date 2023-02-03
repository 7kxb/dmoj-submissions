a = input().split()
for i in range(int(a[1])):
    b = input().split()
    if '-1' in b:
        print(str(a[2]), str(a[3]))
    elif a[1] in b:
        print(str(b[1]), str(b[0]))
    else:
        print(str(b[0]), str(b[1]))