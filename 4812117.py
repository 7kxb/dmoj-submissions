n = int(input())
o = int(input())
a = 0
b = 0
for m in range(1,1000):
    if m-m//n == o:
        if a != 0:
            b = m
        else:
            a = m
    else:
        if b != 0:
            break
        else:
            b = a
print(a,b)