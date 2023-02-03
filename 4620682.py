line1 = input().split()
names = []
distance = []
for i in range(int(line1[0])):
    person = input().split()
    names.append(int(person[0]))
    dist = abs(int(person[1]) - int(line1[1]))
    distance.append(dist)
short = min(distance)
print(names[short])