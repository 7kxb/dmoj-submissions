times = int(input())

total = 1
for i in range(times):
    delta = str(input())
    if delta == 'A':
        total *= 1
    if delta == 'B':
        total *= 0.8
    if delta == 'C':
        total *= 0.6
    if delta == 'D':
        total *= 0.4
    if delta == 'E':
        total *= 0.2

print("{:.6f}".format(total))