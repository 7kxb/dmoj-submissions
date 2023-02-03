from itertools import combinations
distance = int(input())
clubs = int(input())
list = []
prints = 0
toggle = 1
for i in range(clubs):
    swing = int(input())
    if clubs <= 4:
        for i in range(4):
            list.append(swing)
    elif clubs > 4 and clubs <= 16:
        for i in range(2):
            list.append(swing)
    else:
        if int(swing/2) in list:
            if prints == 0 and toggle < 3:
                print('Roberta acknowledges defeat.')
            prints += 1
        elif swing%4 < 3:
            for i in range(2):
                list.append(swing)
            toggle += 1
        else:
            toggle += 1
for x in range(len(list)):
    for y in combinations(list, x+1):
        if sum(y) == distance and prints != 1:
            print('Roberta wins in', str(len(y)), 'strokes.')
            prints += 1
if prints == 0:
    print('Roberta acknowledges defeat.')