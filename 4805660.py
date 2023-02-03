n,m,k = map(int,input().split())
x = [-1 for i in range(n)]
y = [-1 for i in range(n)]
for i in range(k):
    a,b,c = map(int,input().split())
    if c > x[b-1]:
        x[b-1] = c 
        y[b-1] = a 
z = ''
for i in range(n):
    z += str(y[i]) + ' '
print(z)