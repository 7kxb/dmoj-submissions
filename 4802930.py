import math
n = int(input())
x = int(input())
a = 0
for i in range(n):
    p1,p2 = map(int, input().split())
    if abs(p1-p2) > x:
        p3 = int(input())
        a += p3
    else:
        a += max(p1,p2)
print(a)