n = int(input())
x = list(map(int,input().split()))
a = sum(x)
b = a//n
c = 0
for i in range(n):
    if x[i] != b:
        c += 1 
print(c)