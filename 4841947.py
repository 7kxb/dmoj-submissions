n = int(input())
a = []
for i in range(n):
    b = input()
    if b not in a:
        a.append(b)
print(len(a))