n = int(input())
a = ""
for i in range(n):
    if i % 3 == 1:
        a += "_"
    else:
        a += "M"
print(a.count("M"))
print(a)