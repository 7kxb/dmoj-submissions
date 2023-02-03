n = int(input())
a = []
b = list(map(int,input().split()))
c = 0
for i in range(n):
    if b[i] not in a:
        c += 1
        a.append(b[i])
print(c)