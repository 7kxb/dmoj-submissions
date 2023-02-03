a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
x = 0
y = 0
for i in range(s):
    x += a 
    y += b 
    x -= c 
    y -= d 
if x > y:
    print('Nikky')
elif x < y:
    print('Byron')
else:
    print('Tied')