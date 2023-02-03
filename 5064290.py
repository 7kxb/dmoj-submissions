n = int(input())
a = ""
for i in range(n):
    if n >= 5:
        if i % 3 == 0:
            a += "_"
        else:
            a += "M"
    else:
        if i % 2 == 1:
            a += "_"
        else:
            a += "M"
print(a.count("M"))
print(a)