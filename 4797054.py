a = 0
b = 0
for i in range(1,6):
    c = sum(map(int,input().split()))
    if c > a:
        a = c 
        b = i
print(b,a)