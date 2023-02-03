n = int(input())
a = input().split()
e = []
for i in range(len(a)):
    e.append(int(a[i]))
e.sort()
b = int(e[0]/2)
c = e[1]
d = c - b
print(b, d)