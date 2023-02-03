a = input().split()
if len(a[0]) != 3 and len(a[1]) != 7:
    print('invalid')
elif a[0] == 416:
    print('valuable')
elif a[0] != 647 or a[0] != 437:
    print('invalid')
else:
    print('valueless')