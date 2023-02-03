towers = int(input())
list = []
tower = input().split()
for i in range(towers):
    list.append(int(tower[i]))
sight = '0 1'
for i in range(towers-2):
    if i == 0:
        temp = i+2
        if list[i+1] > list[i]:
            temp -= i+1
        sight += ' ' + str(temp)
    else:
        temp = i+2
        if list[i+1] > list[i]:
            temp -= i+1
        elif list[i] > list[i-1]:
            temp -= i
        sight += ' ' + str(temp)
print(sight)