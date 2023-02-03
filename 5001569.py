n = int(input())
t = int(input())
q1 = []
w2 = []
for i in range(t):
    r,c = map(int,input().split())
    q1.append(r)
    w2.append(c)
q1.sort()
w2.sort()
c = 0
a = 1
for i in range(len(q1)):
    b = q1[i]-a
    a = q1[i]
    if b > c:
        c = b
a = 1
for i in range(len(w2)):
    b = w2[i]-a
    a = w2[i]
    if b > c:
        c = b
print(c)