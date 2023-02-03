nodes = []
a = int(input())
c = 1
for i in range(1,a+1):
    for j in range(1,a+1):
        b = input()
        for k in range(1,a+1):
            if b[k-1] == 'A':
                start = c
                nodes.append(c)
            if b[k-1] == '.':
                nodes.append(c)
            if b[k-1] == 'B':
                end = c
                nodes.append(c)
            c += 1
print(nodes)
x = start
y = end
z = 0
toggle = 1
while x != y:
    if x+a*a*toggle in nodes:
        x += a*2*toggle
        z += 1
    elif x+a in nodes:
        x += a*toggle
        z += 1
    elif x+1 in nodes:
        x += 1*toggle
        z += 1 
    else:
        toggle *= -1
        print(10)
        break
print(z)