n,p = map(int,input().split())
names = []
for i in range(n):
    name = input()
    names.append(name)
times = []
for i in range(p):
    time = input().split()
    for j in range(n):
        if i == 0:
            times.append(int(time[j]))
        else:
            times[j] += int(time[j])
for i in range(n):
    names[i] = (names[i],times[i])
names.sort(key=lambda z: z[1])
for i in range(3,n+3):
    print(str(i)+'.',names[i-3][0])