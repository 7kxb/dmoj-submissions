a = list(sorted(map(int, input().split(' '))))
b = input()
c = {'A':0,'B':1,'C': 2}
d = ''
for i in b:
    print(a[c[i]],end=' ')