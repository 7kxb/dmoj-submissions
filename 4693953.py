def chk(n):
    if n <= 1 or (n%2==0 and n!= 2):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True
for _ in range(5):
    n = input()
    b = ''
    for i in range(10):
        a = n.replace('_',str(i))
        if chk(int(a)) == True:
            b += str(i) + ' '
    if b != '':
        print(b)
    else:
        print('Not possible')