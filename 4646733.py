n = int(input())
for i in range(n):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    if a*b != c:
        print('16 BIT S/W ONLY')
    elif a*b == c:
        print('POSSIBLE DOUBLE SIGMA')