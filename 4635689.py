n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
v.sort()
s = 9999999999
for i in range(1, len(v)-1):
    l = (v[i] - v[i-1])/2
    r = (v[i+1] - v[i])/2
    if l + r < s:
        s = l + r
print(s)