n = int(input())
cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
a = 10
for i in range(n):
    case = int(input())
    cases[case-1] = 0
    a -= 1
b = 0
for i in range(10):
    b += cases[i]
c = int(b/a)
d = int(input())
if c > d:
    print('no deal')
else:
    print('deal')