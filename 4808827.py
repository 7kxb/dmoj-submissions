n = int(input())
c = 0
for i in range(n):
    r,g,b = map(int,input().split())
    if 240 <= r and r <= 255 and 0 <= g and g <= 200 and 95 <= b and b <= 220:
        c += 1
print(c)