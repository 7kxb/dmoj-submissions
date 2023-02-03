r = int(input())
a = 100
b = a
for _ in range(r):
    d = input().split()
    if int(d[0]) > int(d[1]):
        b -= int(d[0])
    elif int(d[0]) < int(d[1]):
        a -= int(d[1])
    else:
        pass
print(a)
print(b)