from fractions import Fraction
n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    f = Fraction(b, a)
    g = Fraction(d, c)
    if f > 1 + f / g:
        print('YES')
    else:
        print('NO')