g = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
p = [0, 0, 0, 0, 0]
f = int(input())
n = int(input())
def c(l, p, g, w):
    if w == 1:
        p[g[0]] += 3
    elif w == 0:
        p[g[0]] += 1
        p[g[1]] += 1
    elif w == -1:
        p[g[1]] += 3
    if not l:
        for i in range(1, 5):
            if i != f:
                if p[i] >= p[f]:
                    return False
        return True
    u = l.pop()
    return sum([c(list(l), list(p), u, k) for k in range(-1, 2)])
for _ in range(n):
    a, b, x, y = map(int, input().split())
    if [a, b] in g:
        g.remove([a, b])
    if x > y: 
        p[a] += 3
    if y > x: 
        p[b] += 3
    if x == y:
        p[a] += 1
        p[b] += 1
print(c(g, p, [], 2))