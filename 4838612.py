n = int(input())
for i in range(1000000):
    n += 1
    a = str(n)
    if '0' in a:
        pass
    else:
        print(a)
        break