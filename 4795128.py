n = int(input())
if n == 1:
    print('1 кочерга')
if n >= 2 and n <= 4:
    print(str(n),'кочерги')
if n >= 5:
    if str(n)[-2] != 1 and str(n)[-1] != 1:
        print(str(n),'кочерга')
    elif str(n)[-2] != 1 and str(n)[-1] >= 2 and str(n)[-1] <= 4:
        print(str(n),'кочерги')
    else:
        print('4 кочерги и ещё',str(n-4))