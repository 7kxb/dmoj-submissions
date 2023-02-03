m,n = map(int,input().split())
r = 0
b = 0 
y = 0
for i in range(n):
    a = input()
    for j in range(m):
        if a[i] == '.':
            pass 
        elif a[i] == 'R':
            r += 1
        elif a[i] == 'U':
            b += 1
        elif a[i] == 'Y':
            y += 1 
        elif a[i] == 'O':
            r += 1 
            y += 1 
        elif a[i] == 'G':
            b += 1 
            y += 1 
        elif a[i] == 'P':
            r += 1 
            b += 1 
        elif a[i] == 'B':
            r += 1 
            b += 1 
            y += 1
print(r,b,y)