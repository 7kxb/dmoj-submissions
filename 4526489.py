month = int(input())
day = int(input())

if month == 1:
    print('Before')

if month == 2:
    if day < 18:
        print('Before')
    elif day == 18:
        print('Special')
    elif day > 18:
        print('After')

if month >= 3:
    print('After')