n,m = map(int,input().split())
a = int(input())
t = True
j = []
k = []
for i in range(a):
    x,y = map(int,input().split())
    j.append(x)
    k.append(y)
c = 0
i = 0
while t:
    if c == j[i]:
        i += 1 
        n += k[i]
    if n <= 0:
        print('melt',str(c))
        t = False
    if n >= m:
        print('jam',str(c))
        t = False
    c += 1
    n -= 1