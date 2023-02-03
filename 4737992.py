n = int(input())
x = 0 
for i in range(n):
    p = input()
    a = int(p[:-1])
    b = int(p[-1:])
    c = a**b
    x += c
print(x)