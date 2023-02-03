A = int(input())

while True:
    for i in range(2, A):
        if (A % i) == 0:
            A += 1
        else:
            print(A)
            exit()