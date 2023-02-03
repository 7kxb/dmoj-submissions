t = int(input())
for i in range(t):
    a, b, c, d = map(float, input().split())
    if b > a or d > c:
        X = 0
        Y = 0
        while X <= 100 or Y <= 100:
            X += 10
            Y += 20
            if X*(b/a) >= X+Y or Y*(d/c) >= X+Y:
                print('YES')
            else:
                X = 0
                Y = 0
                while X <= 100 or Y <= 100:
                    X += 20
                    Y += 10
                    if X*(b/a) >= X+Y or Y*(d/c) >= X+Y:
                        print('YES')
                    else:
                        print('NO')
    else:
        print('NO')