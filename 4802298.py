import math
a = int(input())
for i in range(a):
    b = int(input())
    print(math.factorial(b)%(2**32-5))