d = 0
b = 0 
s = 0
r = 0

n = int(input())
for i in range(n):
    a = input()
    if a[0] == 'D':
        d += 1
    if a[0] == 'B':
        b += 1
    if a[0] == 'S':
        s += 1
    if a[0] == 'R':
        r += 1

for i in range(4):
    if max(d,b,s,r) == d and d != 0:
        print('Deluxe Tuna Bitz',str(d))
        d = 0
    if max(d,b,s,r) == b and b != 0:
        print('Bonito Bitz',str(b))
        b = 0
    if max(d,b,s,r) == s and s != 0:
        print('Sashimi',str(s))
        s = 0
    if max(d,b,s,r) == r and r != 0:
        print('Ritzy Bitz',str(r))
        r = 0