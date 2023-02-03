from itertools import combinations
distance = int(input())
clubs = int(input())
swings = 0
total = 0
list = [0]
possibilities = []
prints = 0
for i in range(clubs):
    swing = int(input())
    for i in range(4):
        list.append(swing)
for x in range(1, len(list)+1):
    for y in combinations(list, x):
        if sum(y) == distance and prints != 1:
            possibilities.append(y)
            print('Roberta wins in', str(len(possibilities[0])), 'strokes.')
            prints += 1
if len(possibilities) == 0:
    print('Roberta acknowledges defeat.')