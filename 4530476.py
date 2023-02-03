times = int(input())
list = []

for i in range(times):
    amount = int(input())
    list.append(amount)
    list.sort()

print(list[times-1]-list[0])