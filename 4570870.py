a = int(input())
counter = 0
for i in range(a):
    b = input().split()
    if int(b[0]) > int(b[1]):
        counter += 1 
print(counter)