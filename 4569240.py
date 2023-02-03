tests = int(input())
results = []
for i in range(tests):
    cars = int(input())
    top = []
    mid = []
    bot = []
    for i in range(cars):
        temp = int(input())
        top.append(temp)
    while top[len(top)-1] != 1:
        mid.append(top[len(top)-1])
        top.pop(len(top)-1)
    next = 1 
    top.pop(top.index(1))
    bot.append(next)
    next += 1
    while len(top) > 0 or len(mid) > 0:
        if len(top) > 0 and len(mid) > 0:
            if mid[len(mid)-1] == next:
                mid.pop(len(mid)-1)
                bot.append(next)
                next += 1
            elif top[len(top)-1] == next:
                top.pop(len(top)-1)
                bot.append(next)
                next += 1
            else:
                mid.append(top[len(top)-1])
                top.pop(len(top)-1)
        elif len(mid) > 0:
            if mid[len(mid)-1] == next:
                mid.pop(len(mid)-1)
                bot.append(next)
                next += 1 
            else: 
                results.append('N')
                break
        else:
            if top[len(top)-1] == next:
                top.pop(len(top)-1)
                bot.append(next)
                next += 1 
            else:
                mid.append(top[len(top)-1])
                top.pop(len(top)-1)
    counter = 0
    if len(bot) == cars:
        for j in range(cars):
            if bot[j] == j+1:
                counter += 1
            if counter == cars:
                results.append('Y')
for i in range(tests):
    print(results[i])