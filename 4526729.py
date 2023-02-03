lines = int(input())
list = []
counter = 0
for i in range(lines):
    temp = int(input())
    if temp == 0:
        list.pop()
    else:
        list.append(temp)
if list == []:
  print('0')
else:
  print(sum(list))