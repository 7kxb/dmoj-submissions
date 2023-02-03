from collections import deque
a = 2
b = input()
d = deque()
for c in b:
    if d and c == ')' and d[-1] == '(':
        d.pop()
    else:
        d.append(c)
if not d:
    print('YES')
else:
    if len(d) == a:
        if d[0] == d[1]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')