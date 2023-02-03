k,d = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if a == [0]:
    print(-1)
elif a[0] == 0:
    b = a[1]
    if k <= 2:
        print(str(b)*k)
    elif k > 2:
        c = k-2
        print(str(b)+str(0)*c+str(b))
elif a[0] > 0:
    b = a[0]
    print(str(b)*k)