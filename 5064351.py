n = int(input())
a = "_"
b = n - 2
for i in range(b):
    if i % b == 0 or i % b == b-1:
        a += "M"
    else:
        a += "_"
a += "_"
print(a.count("M"))
print(a)n = int(input())
b = n - 2
a = "_"+"M"*b+"_"
print(a.count("M"))
print(a)