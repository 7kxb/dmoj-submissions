t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    h = a**2 + b**2
    if h > c**2: print('A')
    if h == c**2: print('R')
    if h < c**2: print('O')