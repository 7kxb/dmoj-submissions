p = int(input())
n = int(input())
r = int(input())
a = 0
while p > n:
    a += 1
    n += r*n
    if n > p:
        print(a)