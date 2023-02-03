for i in range(5):
    h = int(input())
    v = int(input())
    x = 50
    y = 25
    while x > 0 and x < 100 and y > 0 and y < 50:
        x += h 
        y += v 
    print(str(x)+','+str(y))