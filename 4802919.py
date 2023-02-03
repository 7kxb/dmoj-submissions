n,c = map(int, input().split())
for i in range(n):
    s,x = input().split()
    if int(x) > c:
        print(s,'will advance')
    else:
        print(s,'will not advance')