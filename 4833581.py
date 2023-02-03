for i in range(5):
    a = int(input())
    b = 5-abs(a)
    c = abs(a)
    if a < 0:
        print('-'*b+'*'*c+'|-----')
    elif a > 0:
        print('-----|'+'*'*c+'-'*b)
    else:
        print('-----|-----')