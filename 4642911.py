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
    f = e[3]
    d = c - b
    g = f - b
    print(b, d, g)

# 3 6 9
# 3 3  6
# 3 6  9
# 3 9  12
# 6 3  9
# 6 6  12
# 6 9  15
# 9 3  12
# 9 6  15
# 9 9  18