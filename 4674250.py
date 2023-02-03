def bfs(nodes, n, p, q):
    check = []
    for i in range(n):
        check.append(False)
    buffer = []
    for i in a[p]:
        buffer.append(i)
    while len(buffer) > 0:
        h = buffer.pop(0)
        if h == q:
            return True
        if not v[h]:
            v[h] = True
            for i in a[h]:
                buffer.append(i)
    return False
    
a = input()
n = int(a[0])
m = int(a[1])

nodes = []
for i in range(n):
    line = []
    nodes.append(line)

for i in range(m+1):
    b = input()
    p = int(b[0]) - 1
    q = int(b[1]) - 1
    if i != m:
        nodes[p].append(q)

if bfs(nodes, n, p, q):
    print('yes')
elif bfs(nodes, n, p, q):
    print('no')
else:
    print('unknown')