from itertools import combinations
distance = int(input())
clubs = int(input())
swings = 0
total = 0
list = [0]
possibilities = []
for i in range(clubs):
    swing = int(input())
    for i in range(distance):
        list.append(swing)
for x in range(1, len(list)+1):
    for y in combinations(list, x):
        if sum(y) == distance:
            possibilities.append(y)
            print('Roberta wins in', len(possibilities[0]), 'strokes.')
            exit()
if len(possibilities) == 0:
    print('Roberta acknowledges defeat.')