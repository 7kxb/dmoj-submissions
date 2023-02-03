import itertools
for _ in range(5):
    n = int(input())
    file = []
    data = []
    for _ in range(n):
        s = int(input())
        file.append(s)
    for i in range(n):
        comb = itertools.combinations(file, i+1)
        for j in comb:
            temp = 0
            for k in range(len(j)):
                temp += j[k]
            if temp <= 1440:
                data.append(temp)
    data.sort()
    print(1440-data[len(data)-1])