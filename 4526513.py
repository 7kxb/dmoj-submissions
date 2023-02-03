string = str(input())

happy = 0
sad = 0

if ':-)' in string:
    happy += string.count(':-)')

if ':-(' in string:
    sad += string.count(':-(')
    
if happy == 0 and sad == 0:
    print('none')

if happy == sad and happy != 0:
    print('unsure')
    
if happy > sad:
    print('happy')
    
if sad > happy:
    print('sad')