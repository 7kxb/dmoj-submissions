a = int(input())
b = int(input())
c = int(input())
d = int(input())

calories = 0


if a == 1:
    calories += 461
if a == 2:
    calories += 431
if a == 3:
    calories += 420
if b == 1:
    calories += 100
if b == 2:
    calories += 57
if b == 3:
    calories += 70
if c == 1:
    calories += 130
if c == 2:
    calories += 160
if c == 3:
    calories += 118
if d == 1:
    calories += 167
if d == 2:
    calories += 226
if d == 3:
    calories += 75
    
print('Your total Calorie count is '+str(calories)+'.')