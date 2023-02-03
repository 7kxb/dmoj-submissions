for _ in range(5):
    n = int(input())
    a = list(map(int, input().split()))
    b = [n]
    for i in range(n-2, -1, -1):
        b.insert(0, n-a[i])
    for i in range(0, n):
        b[i] = a[i]
    print(b)