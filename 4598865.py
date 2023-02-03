from itertools import combinations
distance = int(input())
clubs = int(input())
swings = 0
total = 0
list = []
possibilities = []
for i in range(clubs):
    swing = int(input())
    list.append(swing)
for x in range(clubs):
    for y in combinations(list, x+1):
        if sum(y) == distance:
            possibilities.append(y)
if len(possibilities) == 0:
    print('Roberta acknowledges defeat.')
else:
    print('Roberta wins in', len(possibilities[0]), 'strokes.')