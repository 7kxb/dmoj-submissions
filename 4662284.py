a,b = map(int, input().split())
c = round(a/b*1000, 2)
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    if round(x/y*1000, 2) < c:
        c = round(x/y*1000, 2)
print(format(c, '.2f'))