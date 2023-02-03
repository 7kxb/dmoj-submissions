n = int(input())
b = 0
for _ in range(n):
    a = input()
    for i in range(len(a)):
        if a[i] == 'A':
            b += 4 
        elif a[i] == 'K':
            b += 3 
        elif a[i] == 'Q':
            b += 2 
        elif a[i] == 'J': 
            b += 1
print(b)