d1 = int(input())
d2 = int(input())
ways = 0
for i in range(1, d1+1):
    for j in range(1, d2+1):
        if i+j == 10:
            ways += 1
if ways != 1:
    print("There are", ways, "ways to get the sum 10.")
else:
    print("There is", ways, "way to get the sum 10.")