tileA = 1
tileB = 2
tileC = 3
tileD = 4

line = input()
amount = len(line)


counter = 0
for i in range(amount):
    tempA = tileA
    tempB = tileB
    tempC = tileC
    tempD = tileD
    if line[counter] == 'H':
        tileA = tempC
        tileB = tempD
        tileC = tempA
        tileD = tempB
    if line[counter] == 'V':
        tileA = tempB
        tileB = tempA
        tileC = tempD
        tileD = tempC
    counter += 1

print(str(tileA), str(tileB))
print(str(tileC), str(tileD))