for _ in range(5):
    a = int(input())
    b = []
    for i in range(a):
        b.append(int(input()))
    b.append(101)
    b.sort()
    c = 1 
    for i in range(a+1):
        if b[i] == c:
            c += 1
        else:
            print(c)
            break