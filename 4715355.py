n = int(input())
k = 0
for i in range(n):
    c, v = map(int, input().split())
    if v > 0:
        k += c 
print(k)