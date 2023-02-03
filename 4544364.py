one = int(input())
two = str(input())
list = two.split()
list.sort()
counter = 0
a = ''
while counter < one:
    a += list[counter] + ' '
    counter += 1
print(a)