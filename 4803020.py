x = int(input())
n = int(input())
a = x
for i in range(n):
    p = int(input())
    b = x - p 
    a += b
print(a)