n = int(input())
if n == 2:
    a = input().split()
    e = []
    for i in range(len(a)):
        e.append(int(a[i]))
    e.sort()
    b = int(e[0]/2)
    c = e[1]
    d = c - b
    print(b, d)
if n == 3:
    a = input().split()
    e = []
    for i in range(len(a)):
        e.append(int(a[i]))
    e.sort()
    b = int(e[0]/2)
    c = e[2]
    f = e[4]
    d = c - b
    g = f - b
    print(e)
    print(b, d, g)
if n >= 3:
    a = input().split()
    e = []
    for i in range(len(a)):
        e.append(int(a[i]))
    e.sort()
    b = int(e[0]/2)
    s = ''
    for i in range(n):
        h = e[i*2]
        k = h - b
        s += str(k) + ' '
    print(s)
    

# 1 3 6 7

# 1 1 - 2
# 1 3 - 4
# 1 6 - 7
# 1 7 - 8

# 3 1 - 4
# 3 3 - 6
# 3 6 - 9
# 3 7 - 10

# 6 1 - 7
# 6 3 - 9
# 6 6 - 12
# 6 7 - 13

# 7 1 - 8 
# 7 3 - 10 
# 7 6 - 13 
# 7 7 - 14