v = []
for i in range(3):
    v.append(int(input()))
if v[1] >= v[0] and v[2] >= v[1]:
    print('Good job!')
else:
    print('Try again!')