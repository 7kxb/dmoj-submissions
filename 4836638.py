n = int(input())
c = []
for i in range(n):
    a,b = map(str,input().split())
    b = float(b)
    c.append([b,a])
c.sort()
print(c[-1][-1])