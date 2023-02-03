def isPrime(n):
    if n <= 1 or (n%2==0 and n!= 2):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True
def nextPrime(n):
    if n <= 1:
        return 2
    prime = n
    found = False
    while not found:
        prime = prime + 1
        if isPrime(prime) == True:
            found = True
    return prime
n = int(input())
if isPrime(n):
    print(n)
else:
    print(nextPrime(n))