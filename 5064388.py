n = int(input())
a = "_"
b = n - 2
for i in range(b):
    if i % b == 0 or i % b == n//4+1:
        a += "M"
    else:
        a += "_"
a += "_"
print(a.count("M"))
print(a)