def createSieve(a,b):
    sieve = [False, False] + [True] * (b-1)
    for i in range(2, b-1):
        if sieve[i] == True:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False
    z = []
    for i in range(len(sieve)):
        if sieve[i] == True and i >= a:
            z.append(i)
    return sum(z)
for i in range(int(input())):
    a,b = map(int,input().split())
    print(createSieve(a,b))