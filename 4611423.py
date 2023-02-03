unusable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'M', 'O', 'P', 'R', 'T', 'U', 'V', 'W', 'Y']
sign = input()
toggle = True
for i in range(19):
    if unusable[i] in sign:
        toggle = False
if toggle:
    print('YES')
else:
    print('NO')