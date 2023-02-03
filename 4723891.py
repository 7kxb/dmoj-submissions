a = list(map(int,input().split()))
def b(c):
    if c == len(d):
        print(len(d))
        return
    e = d[:c+1]
    f = True
    for i in range(0,len(d),len(e)):
        if len(d)-1 < len(e):
            if e[:len(d)-1] != d[i:i+len(e)]:
                f = False
            break
        if d[i:i+len(e)] != e:
            f = False
    if e:
        print(len(e))
        return
    b(c+1)
while a[0] != 0:
    if a[0] == 1:
        print(0)
        a = list(map(int,input().split()))
        continue
    d = [a[i]-a[i-1] for i in range(2,a[0]+1)]
    b(0)
    a = list(map(int,input().split()))