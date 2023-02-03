n = int(input())
if n == 1:
    print('1 кочерга')
if n >= 2 and n <= 4:
    print(str(n),'кочерги')
if n >= 5:
    print('4 кочерги и ещё',str(n-4))