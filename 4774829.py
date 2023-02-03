n = int(input())
a = []
c = 0
for i in range(n):
    b = int(input())
    if b not in a:
        c += 1 
        a.append(b)
print(c)