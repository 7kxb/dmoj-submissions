a = int(input())
b = []
for i in range(a):
    b.append(i+1)
c = ''
for i in range(a):
    d = input().split()
    if int(d[0]) == 0:
        c += str(i+1) + ' '
        b.pop(b.index(i+1))
    else:
        counter = 0
        for j in range(int(d[0])):
            if int(d[j+1]) in b:
                counter -= 1
            else:
                counter += 1
                if counter == int(d[0]):
                    c += str(i+1) + ' '
                    b.pop(b.index(i+1))
for i in range(len(b)):
    if i != len(b)-1:
        c += str(b[i]) + ' '
    else:
        c += str(b[i])
print(c)