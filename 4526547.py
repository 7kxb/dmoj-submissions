a = int(input())

b = []
for i in range(a):
    c = str(input())
    b.append(c)

d = []
for i in range(a):
    e = str(input())
    d.append(e)

f = 0
while a >= 0:
    a -= 1
    if b[a] == d[a]:
        f += 1

print(f)