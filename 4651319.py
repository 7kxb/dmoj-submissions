n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append(int(a[i]))
b.sort()
c = ''
for i in range(n):
    c += str(b[i]) + ' '
print(c)