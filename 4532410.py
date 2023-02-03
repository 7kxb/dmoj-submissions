distance = int(input())
clubs = int(input())
total = 0
for i in range(clubs):
    add = int(input())
    total += add
if distance == total:
    print('Roberta wins in ' + str(clubs) +' strokes.')
else:
    print('Roberta acknowledges defeat.')