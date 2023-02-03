A = int(input())
B = A 

while B >= A:
    for i in range(B):
        if B % (i + 1) == 0:
            B += 1
        else:
            print(B)
            exit()