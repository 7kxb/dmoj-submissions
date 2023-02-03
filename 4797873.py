n,m = map(int,input().split())
a = [[0 for i in range(n)]for i in range(n)]
b = 0
for i in range(m):
    x,y,w,h = map(int,input().split())
    for j in range(w):
        for k in range(h):
            a[x+j][y+k] += 1
            if a[x+j][y+k]%2 == 0:
                b -= 1
            else:
                b += 1
#for i in range(n):
    #print(a[i])
print(b)