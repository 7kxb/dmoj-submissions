n = int(input())
a = input()
b = 0
for i in range(n):
    if a[i] == 'L':
        b += 0.5
if n+1-b > n:
    print(n)
else:
    print(int(n+1-b))