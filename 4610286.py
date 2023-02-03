import re
toggle = True
while toggle:
    string = input()
    if string == 'quit!':
        quit()
    elif 'or' in string and len(string) > 3:
        print(re.sub(r'or', r'our', string))
    else:
        print(string)