q = int(input())
for i in range(q):
    abc = input().split()
    m = int(abc[2]) % int(abc[0])
    n = int(abc[0]) * int(abc[1]) + m
    print(n)