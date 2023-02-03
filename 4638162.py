import itertools
n = int(input())
a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()
f = []
for i in range(len(b)):
    c = b[i]
    e = []
    for i in range(1, b[i]):
        e.append(i)
        e.append(i)
        e.append(i)
    d = [seq for i in range(len(e), 0, -1)
          for seq in itertools.combinations(e, i)
          if sum(seq) == c]
    f.append(d[-1])
g = ''
if n == 2:
    g += str((f[0][0])) + ' '
    g += str((f[-1][1]))
if n == 3:
    g += str((f[0][0])) + ' '
    g += str((f[4][1])) + ' '
    g += str((f[-1][1]))
print(g)