number = int(input())
list = []

for i in range(number):
    temp = int(input())
    list.append(temp)
    
list.sort()

counter = 0
for i in range(number):
    print(list[counter])
    counter += 1