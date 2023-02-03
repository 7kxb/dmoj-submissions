width = int(input())
percent = int(input())

if width == 3 and percent >= 95:
    print('C.C. is absolutely satisfied with her pizza.')
elif width == 1 and percent <= 50:
    print('C.C. is fairly satisfied with her pizza.')
else:
    print('C.C. is very satisfied with her pizza.')