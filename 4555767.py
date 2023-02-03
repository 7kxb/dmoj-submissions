question = int(input())
N = int(input())
line3 = input().split()
line4 = input().split()
list1 = []
list2 = []
for i in range(N):
    list1.append(int(line3[i]))
    list2.append(int(line4[i]))
list1.sort()
list2.sort()
sum = 0
if question == 1:
    for i in range(N):
        sum += max(list1[i], list2[i])
else:
    for i in range(N):
        sum += max(list1[i], list2[N-1-i])
print(sum)