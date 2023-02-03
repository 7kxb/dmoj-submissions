n = int(input())
a = input().split()
c = 0
for i in range(n):
    if len(a[i]) <= 10:
        c += 1
print(c)