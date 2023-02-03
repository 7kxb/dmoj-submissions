n, m = map(int, input().split())
list = []
a = 0
for i in range(n):
    item = input()
    list.append(item)
for i in range(m):
    n = int(input())
    x = True
    for i in range(n):
        item2 = input()
        if item2 not in list:
            x = False 
    if x:
        a += 1 
print(a)