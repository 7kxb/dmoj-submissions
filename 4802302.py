import math
a = int(input())
for i in range(a):
    b = int(input())
    if b <= 33:
        print(math.factorial(b)%(2**32-5))
    else:
        print(0)