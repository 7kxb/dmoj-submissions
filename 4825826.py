n = int(input())
size = 541
sieve = [False, False] + [True] * (size-1)
for i in range(2, size-1):
    if sieve[i] == True:
        for j in range(2*i, len(sieve), i):
            sieve[j] = False
for i in range(542):
    if sieve[i] == True:
        if n != 0:
            print(i)
            n -= 1