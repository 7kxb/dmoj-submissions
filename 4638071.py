n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append(int(a[i]))
b.sort()
for i in range(1,b[0]+1):
    check = 0
    for j in range(n):
        if b[j]%i == 0:
            check += 1
    if check == n:
        use = i
c = ''
for i in range(n):
    d = int(int(a[i])/use)
    c += str(d) + ' '
print(c)