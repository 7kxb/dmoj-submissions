lines = int(input())
t = 0
s = 0
for i in range(lines):
    temp = str(input())
    characters = len(temp)
    counter = 0
    while counter < characters:
        if temp[counter] == 't' or temp[counter] == 'T':
            t += 1
        if temp[counter] == 's' or temp[counter] == 'S':
            s += 1
        counter += 1 
if t > s:
    print('English')
if t < s:
    print('French')
if t == s:
    print('French')