import math
r = int(input())
m = int(input())
z = []
for i in range(r):
    x,y = map(int, input().split())
    z.append([x,y])
z.sort()
z.append([1000,1000])
a = []
j = z[0][0]
k = z[0][1]
for i in range(r+1):
    if z[i][0] == j:
        if z[i][1] > k:
            k = z[i][1]
    else:
        if z[i][0] > j and z[i][1] > k:
            a.append([j,k])
            j = z[i][0]
            k = z[i][1]
        else:
            a.append([j,k])
            j = z[i+1][0]
            k = z[i+1][1]
b = []
j = z[0][0]
k = z[0][1]
for i in range(r+1):
    if z[i][0] == j:
        if z[i][1] < k:
            k = z[i][1]
    else:
        if z[i][0] > j and z[i][1] > k:
            b.insert(0,[j,k])
            j = z[i][0]
            k = z[i][1]
        else:
            b.insert(0,[j,k])
            j = z[i+1][0]
            k = z[i+1][1]
c = a[0:len(a)+1] + b[0:len(b)+1] 
f = []
for w in c:
    if w not in f:
        f.append(w)
f += a[0:1]
h = 0
print(f)
for i in range(len(f)-1):
    d = abs(f[i][0] - f[i+1][0])
    e = abs(f[i][1] - f[i+1][1])
    g = d**2 + e**2
    h += math.ceil(math.sqrt(g)) * m
print('$'+str(h)+'.00')
# 5
# 1 
# 1 1
# 1 3
# 2 4
# 3 2
# 3 1