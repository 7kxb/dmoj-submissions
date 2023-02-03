import math
p = int(input())
for i in range(p):
    n = int(input())
    print(math.factorial(n)%2**32)