def createSieve(size):
    sieve = [False, False] + [True] * (size-1)
    for i in range(2, size-1):
        if sieve[i] == True:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False
    return sieve
n = int(input())
a = createSieve(n)
for i in range(1,n+1):
    if a[i]:
        print('1')
    else:
        print('0')