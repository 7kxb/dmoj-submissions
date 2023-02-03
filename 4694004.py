n = int(input())
if n == 0:
    print('9')
elif n == 4:
    print('198')
elif n%2 == 0:
    a = n-4 - int((n-5)/2)
    b = ('1'+'9'*a+'8')
    print(int(b)%1000000000)
elif n%2 == 1:
    a = n-4 - int((n-5)/2)
    b = ('1'+'0'+'9'*a+'8')
    print(int(b)%1000000000)