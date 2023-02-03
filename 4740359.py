n = int(input())
c = 0
for i in range(n+1):
    for j in range(i,n+1):
        c += i + j
print(c)