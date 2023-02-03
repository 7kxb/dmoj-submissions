n = int(input())
list = []
counter = 0
for i in range(n):
    point = int(input())
    foul = int(input())
    stars = point*5 - foul*3
    list.append(stars)
for i in range(n):
    if list[i] > 40:
        counter += 1
if counter == n:
    print(str(counter)+'+')
else:
    print(counter)