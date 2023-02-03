n = int(input())
a = list(map(int, input().split()))
a.sort()
x = a[-1]
y = sum(a)
if x <= y/2:
    b = y
elif x > y/2:
    b = 2*x
print(b)