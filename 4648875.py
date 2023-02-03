n = int(input())
a = ''
b = 0
for i in range(n):
    c = str(input())
    d = int(input())
    if d > b:
        a = c
        b = d
print(a)