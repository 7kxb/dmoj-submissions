city = []
temp = []
toggle = True

while toggle:
    data = input()
    if "Waterloo" in data:
        city.append(data.split())
        toggle = False
    else:
        city.append(data.split())

length = len(city)
for i in range(length):
    temp.append(int(city[i][1]))

cold = min(temp)
a = temp.index(cold)
print(city[a][0])