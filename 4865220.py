p,c,v = map(int,input().split())
a = 0
if p%3 != 0:
    a += p//3 + 1 
else:
    a += p//3
if c%3 != 0:
    a += c//3 + 1 
else:
    a += c//3
if v%3 != 0:
    a += v//3 + 1 
else:
    a += v//3
print(a)