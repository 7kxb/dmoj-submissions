cases = {
    1:100,
    2:500,
    3:1000,
    4:5000,
    5:10000,
    6:25000,
    7:50000,
    8:100000,
    9:500000,
    10:1000000
}
n = int(input())
c = 1691600
for i in range(n):
    a = cases.get(int(input()))
    c -= a
b = int(input())
if b > c+a:
    print('deal')
elif b < c+a:
    print('no deal')