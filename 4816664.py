import math
r1,g1,b1 = map(int,input().split())
r2,g2,b2 = map(int,input().split())
c = 0
if int(math.sqrt(r1)) == int(math.sqrt(r2)):
    c += 1
if int(math.sqrt(g1)) == int(math.sqrt(g2)):
    c += 1
if int(math.sqrt(b1)) == int(math.sqrt(b2)):
    c += 1
if c == 3:
    print('Dull')
else:
    print('Colourful')