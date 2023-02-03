b = []
for _ in range(10):
    a = int(input())
    if a%42 not in b:
        b.append(a%42)
print(len(b))