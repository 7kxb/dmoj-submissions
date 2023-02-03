r,c = map(int,input().split())
a,b = map(int,input().split())
for i in range(r):
    for j in range(a):
        z = ''
        for k in range(c):
            if i%2 == k%2:
                z += 'X'*b
            else:
                z += '.'*b
        print(z)