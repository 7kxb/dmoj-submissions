n = int(input())
a = input()
b = 0
if a == 'left':
    b = -1
if a == 'right':
    b = 1
if n%2 == 0:
    b *= -1
if b == -1:
    print('left')
if b == 1:
    print('right')