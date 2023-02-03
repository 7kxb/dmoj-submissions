n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    a = '0'+a
    b = '0'+b
    if a[-2]+a[-1] == '17' or b[-2]+b[-1] == '17':
        print('NO')
    elif a[-1] == '7' and b[-2]+b[-1] == '11':
        print('YES')
    elif b[-1] == '7' and a[-2]+a[-1] == '11':
        print('YES')
    else:
        print('NO')