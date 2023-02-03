a = []
for i in range(9):
    a.append(int(input()))
t = True
for i in range(9):
    for j in range(9):
        if t:
            b = sum(a) - a[i] - a[j]
        if b == 100:
            if i < j:
                a.remove(a[i])
                a.remove(a[j-1])
                for i in range(7):
                    print(a[i])
                b = 0 
                t = False
            elif i > j:
                a.remove(a[i])
                a.remove(a[j])
                for i in range(7):
                    print(a[i])
                b = 0 
                t = False