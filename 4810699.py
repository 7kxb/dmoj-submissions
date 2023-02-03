a = input()
b = a.index('L')
c = a.index('R')
a = a[:b] + 'x' + a[b+1:]
a = a[:c] + 'x' + a[c+1:]
print(b+1,c+1)
b = a.index('L')
c = a.index('R')
print(b+1,c+1)