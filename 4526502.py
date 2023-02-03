string = str(input())

happy = 0
sad = 0

for ':-)' in string:
    happy += 1

for ':-(' in string:
    sad += 1
    
if happy == 0 and sad == 0:
    print('none')

if happy == sad:
    print('unsure')
    
if happy > sad:
    print('happy')
    
if sad > happy:
    print('sad')