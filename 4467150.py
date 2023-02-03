t = int(input())
for i in range(t):
    a, b, c, d = map(float, input().split())
    if b > a*2 or d > c*2:
        X = b/a
        Y = d/c
        if X*(b/a) >= X+Y or Y*(d/c) >= X+Y:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')