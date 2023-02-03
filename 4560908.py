minutes = int(input())
chores = int(input())
list = []

for i in range(chores):
    list.append(int(input()))
list.sort()
counter = 0
time = minutes
for i in list:
    if time - i < 0:
        print(counter)
        break
    else:
        time -= i 
        counter += 1