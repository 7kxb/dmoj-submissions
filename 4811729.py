r,c = map(int,input().split())
a,b = map(int,input().split())
for i in range(r):
    for j in range(a):
        if j%2 == 0:
            z = 'x'*b
            print(z)
        else:
            z = '.'*b
            print(z)
# hold on im just saving my code ill figure this out later (its supposed to be simple, right?)