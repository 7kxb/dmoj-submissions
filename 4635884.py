list = ['A', 'B', 'C', 'D', 'E']
toggle = True
while toggle:
    button = int(input())
    times = int(input())
    for i in range(times):
        if button == 1:
            list.append(list[0])
            list.pop(0)
        if button == 2:
            list.insert(0, list[4])
            list.pop()
        if button == 3:
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
        if button == 4:
            print(list[0], list[1], list[2], list[3], list[4])
            toggle = False