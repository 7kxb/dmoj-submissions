n = int(input())
k = int(input())
m = {}
def p(n, k):
    if n < k: return 0
    if k == n or k == 1: return 1
    if (n, k) in m: return m[(n, k)]
    m[(n, k)] = p(n - 1, k - 1) + p(n - k, k)
    return m[(n, k)]
print(p(n, k))