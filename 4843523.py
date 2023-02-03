t = int(input()):
    a,b,n = map(int,input().split())
    if n % a == 0:
        print('YES')
    else:
        print('NO')