square = 1 
toggle = True
while toggle:
    roll = int(input())
    if roll < 2 or roll > 12:
        print('You Quit!')
        toggle = False
    elif square + roll <= 100:
        square += roll
        if square == 9: 
            square = 34
        if square == 40:
            square = 64
        if square == 67:
            square = 86
        if square == 54:
            square = 19
        if square == 90:
            square = 48
        if square == 99:
            square = 77
        print('You are now on square',str(square))
        if square == 100:
            print('You Win!')
            toggle = False
    else:
        print('You are now on square',str(square))