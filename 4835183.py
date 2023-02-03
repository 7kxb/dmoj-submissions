def isPrime(n):
    if n <= 1 or (n%2==0 and n!= 2):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for i in range(2,2*n):
        a = i 
        b = 2*n-i
        if a+b == 2*n and isPrime(a) and isPrime(b):
            print(a,b)
            break