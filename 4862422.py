a = '*abcdefghijklmnopqrstuvwxyz'
b = input()
c = 0
for i in range(len(b)):
    c += a.index(b[i])
print(c)