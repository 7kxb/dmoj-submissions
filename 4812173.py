a = input()
b = 'A'
for i in range(len(a)):
    if i%2 == 1:
        if a[i-1] == b:
            b = a[i]
if b == 'A':
    print(1)
if b == 'B':
    print(2)
if b == 'C':
    print(3)