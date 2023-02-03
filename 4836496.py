a = input()
v = ['a','e','i','o','u']
t = True
i = 0
while t:
    if a[i] in v:
        a = a[0:i+1] + a[i+3:-1] + a[-1]
        i = 0
    else:
        i += 1
print(a)