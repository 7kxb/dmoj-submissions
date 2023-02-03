A = int(input())

while True:
    for i in range(A):
        if A % (i + 1) == 0:
            A += 1
        else:
            print(A)
            exit()