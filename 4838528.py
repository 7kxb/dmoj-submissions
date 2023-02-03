n = int(input())
a = 0
for i in range(n):
    a += (i+1)**6
print(a%10**9)