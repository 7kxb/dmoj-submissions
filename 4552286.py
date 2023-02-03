a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

a = (a3*3) + (a2*2) + (a1*1)
b = (b3*3) + (b2*2) + (b1*1)

if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('T')