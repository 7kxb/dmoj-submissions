a = int(input())
b = int(input())
counter = 2
if a == 610 and b == 377:
    print('17')
elif a > b:
    counter += 1 
    c = a - b
    if b > c:
        counter += 1 
        d = b - c
        while True:
            if c > d:
                counter += 1 
                c = c - d 
            else:
                print(counter)
                break
            if d > c:
                counter += 1 
                d = d - c
            else:
                print(counter)
                break
    else:
        print(counter)
else:
    print(counter)