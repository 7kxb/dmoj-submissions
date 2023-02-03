n = int(input())
m = int(input())
b = 0
for i in range(m):
    a = int(input())
    if a >= n:
        b += 1
print(b)