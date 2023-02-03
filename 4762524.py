import math
a = 0
h,v = map(int, input().split())
for x in range(1,v+1):
    for y in range(h+1):
        dx = y / math.gcd(x,y+1)
        dy = x / math.gcd(x,y+1)
        xi = x + dx
        yi = y + dy
        while xi <= v and yi <= h:
            a += (h - yi) * (v - xi)
            xi += dy 
            yi += dy
print(math.ceil(a))