t = int(input())
for i in range(t):
    a, b, c, d = map(float, input().split())
    if b > a:
        X = 0
        Y = 0
        while X or Y <= 100:
            X += 2
            Y += 1
            if X*(b/a) >= X+Y or Y*(d/c) >= X+Y:
                print('YES')
        if X or Y >= 100:
            print('NO')
    elif d > c:
        X = 0
        Y = 0
        while X or Y <= 100:
            X += 1
            Y += 2
            if X*(b/a) >= X+Y or Y*(d/c) >= X+Y:
                print('YES')
        if X or Y >= 100:
            print('NO')
    else:
        print('NO')