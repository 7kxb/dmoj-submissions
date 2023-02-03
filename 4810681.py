n = int(input())
b = []
g = []
a = 0
for i in range(n):
    b.append(int(input()))
for i in range(n):
    g.append(int(input()))
for i in range(len(b)):
    x = max(g)
    if x > b[i]:
        a += 1 
        g.remove(x)
print(a)