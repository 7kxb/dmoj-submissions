toggle = True
while toggle:
    string = input()
    if string == 'quit!':
        toggle = False
    elif string[-3] != 'a' and string[-3] != 'e' and string[-3] != 'i' and string[-3] != 'o' and string[-3] != 'u':
        if string[-2] == 'o' and string[-1] == 'r' and len(string) > 3:
            string = string[:-1]
            string += 'ur'
            print(string)
    else:
        print(string)