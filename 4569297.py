a = int(input())
b = []
for c in range(a):
    d = int(input())
    if d in b:
        e = [i for i, x in enumerate(b) if x == d]
        b.pop(e[0])
    else:
        b.append(d)
print(b[0])