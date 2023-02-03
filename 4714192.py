for _ in range(5):
    one = input()
    two = input()
    counter = 0
    if len(one) < len(two):
        for i in range(len(one)):
            if one[i] == two[i]:
                counter += 1
            else:
                break
    else:
        for i in range(len(two)):
            if one[i] == two[i]:
                counter += 1
            else:
                break
    print(counter)