wins = 0
for i in range(6):
    outcome = str(input())
    if outcome == 'W':
        wins += 1
if wins == 0:
    print('-1')
if wins >= 1 and wins <= 2:
    print('3')
if wins >= 3 and wins <= 4:
    print('2')
if wins >= 5 and wins <= 6:
    print('1')