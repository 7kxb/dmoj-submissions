low = int(input())
high = int(input())
rsa = 0
for i in range(low,high+1):
    divisor = 0
    for j in range(1,i+1):
        if i%j == 0:
            divisor += 1
    if divisor == 4:
        rsa += 1
print("The number of RSA numbers between", str(low), "and", str(high), "is", str(rsa))