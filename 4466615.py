t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    if b > a or d > c:
        print('YES')
    else:
        print('NO')