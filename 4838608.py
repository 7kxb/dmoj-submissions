a = input()
b = input()
d = len(b)
if b[d-1] == 'e':
    c = 'la'
elif b[d-1] == 's':
    c = 'les'
else:
    c = 'le'
print(a+'-tu',c,b,'?')