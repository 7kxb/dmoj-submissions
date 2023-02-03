t = int(input())
for i in range(t):
    a, b, c, d = map(float, input().split())
    if b > a or d > c:
        X = 0
        Y = 0
        while X or Y <= 100:
            X += b/a
            Y += d/c
            if X*(b/a) >= X+Y or Y*(d/c) >= X+Y:
                print('YES')
        if X or Y >= 100:
            print('NO')
    else:
        print('NO')