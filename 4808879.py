n = int(input())
a = list(map(int,input().split()))
b = 200 - sum(a)
if b >= 0:
    print(b)
else:
    print('Over maximum capacity!')