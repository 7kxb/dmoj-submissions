def modInverse(n,m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (n > 1) : 
        q = n // m 
        t = m 
        m = n % m 
        n = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x 
n,m = map(int,input().split())
print(modInverse(n,m))