length = int(input())
amount = int(input())
times = int(input())

for i in range(times):
    length -= amount
    print(length)