a = list(map(int, input().split()))
b = a.sort()
if b[0] + b[1] <= b[2]:
    print('no')
else:
    print('yes')