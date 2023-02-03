import math
for _ in range(5):
    n = int(input())
    a = 0
    for i in range(1,int(math.sqrt(n))+1):
        j = i
        while j*i<=n:
            a += 1
            j += 1
    print(a)