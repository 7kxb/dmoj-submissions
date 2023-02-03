n = int(input())
for i in range(n):
    a = input()
    if 'M' in a and 'C' in a:
        print('NEGATIVE MARKS')
    elif 'M' in a or 'C' in a:
        print('FAIL')
    else:
        print('PASS')