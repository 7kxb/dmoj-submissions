n = int(input())
for _ in range(n):
    a = int(input())
    b = input().split()
    c = []
    for i in range(a):
        c.append(int(b[i]))
    d = [c[0]]
    e = True
    for j in range(1,a):
        if c[j] > d[-1]:
            d.append(c[j])
        elif c[j] < d[0]:
            d.insert(0,c[j])
        elif c[0] > d[-1]:
            d.append(c[0])
        elif c[0] > d[0]:
            d.insert(0,c[j])
        else:
            print("Case #"+str(_+1)+": no")
            e = False
            break
    if e:
        print("Case #"+str(_+1)+": yes")