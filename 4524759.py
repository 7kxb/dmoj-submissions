times = int(input())

list = []
for i in range(times):
    temp = int(input())
    list.append(temp);

list.sort();

for a in list:
    print(a);