import random
n = int(input())
a = 0
for i in range(56):
    a += sum(list(map(int,input().split())))
for i in range(n):
    print(a//n)