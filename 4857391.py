n = int(input())
a = list(map(str,input().split()))
b = input()
c = len(b)
d = ''
while d == '':
    for j in range(100):
        for i in range(n):
            if len(a[i]) == c-j and d == '':
                print(a[i])
                d = a[i]