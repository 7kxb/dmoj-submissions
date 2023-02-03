a = int(input())
b = []
for c in range(a):
    d = int(input())
    if d in b:
        b.pop(b.index(d))
    else:
        b.append(d)
print(b[0])