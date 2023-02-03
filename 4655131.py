n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append(int(a[i]))
b.sort()
low = []
high = []
for i in range(int(n/2+.5)):
    low.append(b[i])
for i in range(int(n/2+.5), n):
    high.append(b[i])
low.reverse()
c = ''
for i in range(int(n/2)):
    c += str(low[i]) + ' '
    c += str(high[i]) + ' '
if n%2 != 0:
    c += str(low[-1])
print(c)