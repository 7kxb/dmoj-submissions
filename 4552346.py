lines = int(input())
list = []
for i in range(lines):
    temp = int(input())
    list.append(temp)
list.sort()
pointer = lines - 1
sum = 0
while pointer >= 0:
    sum += list[pointer]
    pointer -= 2
print(sum)