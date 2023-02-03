cases = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
n = int(input())
for i in range(n):
    a = int(input())
    cases.pop(a-1)
for i in range(len(cases)):
    c += cases[i]
d = int(c/len(cases))
b = int(input())
if b > d:
    print('deal')
elif b < d:
    print('no deal')