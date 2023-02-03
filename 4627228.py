n = int(input())
m = 0
while n != 1:
    if n%2 == 1:
        n = 3*n+1
        m += 1
    if n%2 == 0:
        n = n/2
        m += 1
print(m)