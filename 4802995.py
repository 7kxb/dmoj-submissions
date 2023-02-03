n = int(input())
a = 0
for i in range(n):
    x1,x2 = map(int,input().split())
    t = x2-x1
    if t > a:
        a = t
print(a)