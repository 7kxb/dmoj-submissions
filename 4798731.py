n = int(input())
a = []
b = 0
c = []
for i in range(n):
    a.append(int(input()))
a.sort()
while a != []:
    b += 1
    if b%3 != 0:
        c.append(a[-1])
    a.pop()
print(sum(c))