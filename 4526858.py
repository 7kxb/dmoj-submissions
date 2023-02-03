quarters = int(input())
a = 0
b = 0 
c = 0 
a += int(input())
b += int(input())
c += int(input())

counter = 0

while quarters > 0:
    a += 1
    counter += 1
    quarters -= 1
    if a == 35:
        quarters += 30
    if quarters == 0:
        print('Martha plays ' + str(counter) + ' times before going broke.')
    b += 1
    counter += 1 
    quarters -= 1 
    if b == 100:
        quarter += 60
    if quarters == 0:
        print('Martha plays ' + str(counter) + ' times before going broke.')
    c += 1 
    counter += 1
    quarters -= 1
    if c == 10:
        quarters += 9
    if quarters == 0:
        print('Martha plays ' + str(counter) + ' times before going broke.')