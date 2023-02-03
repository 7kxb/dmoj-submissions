n = int(input())
a = input().split()
b = []
for i in range(2*n):
    b.append(int(a[i]))
b.sort()
d = 0
for i in range(1,n+1):
    c = b[i*2-1] - b[i*2-2]
    d += c
print(d)