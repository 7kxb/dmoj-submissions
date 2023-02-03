number = int(input())
list = []
for i in range(number):
    temp = int(input())
    list.append(temp)
list.sort()
for i in range(number):
    print(list[i])