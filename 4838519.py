b = 0
for i in range(len(a)):
    if i%2 == 1:
        b += str(a[i])*2
        a.remove(a[i])
if (b+a)%10 == 0:
    c = True
else:
    c = False