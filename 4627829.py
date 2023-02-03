w = int(input())
i = int(input())
l = int(input())
d = int(input())
c = int(input())
a = int(input())
t = int(input())
s = int(input())
at = int(input())
num = int(input())
star = int(input())
sets = 0
check = 1
while check != 0:
    while w >= 1 and i >= 1 and l >= 1 and d >= 1 and c >= 1 and a >= 1 and t >= 1 and s >= 1:
        sets += 1
        w -= 1
        i -= 1 
        l -= 1 
        d -= 1 
        c -= 1 
        a -= 1 
        t -= 1 
        s -= 1
    if at >= 1 or num >= 1 or star >= 1:
        check = 1
    else:
        check = 0
    if w == 0:
        if num >= 1:
            num -= 1
            w += 1
        elif star >= 1:
            star -= 1
            w += 1
    if i == 0:
        if at >= 1:
            at -= 1
            i += 1
        elif star >= 1:
            star -= 1
            i += 1
    if l == 0:
        if num >= 1:
            num -= 1
            l += 1
        elif star >= 1:
            star -= 1
            l += 1
    if d == 0:
        if num >= 1:
            num -= 1
            d += 1
        elif star >= 1:
            star -= 1
            d += 1
    if c == 0:
        if num >= 1:
            num -= 1
            c += 1
        elif star >= 1:
            star -= 1
            c += 1
    if a == 0:
        if at >= 1:
            at -= 1
            a += 1
        elif star >= 1:
            star -= 1
            a += 1
    if t == 0:
        if num >= 1:
            num -= 1
            t += 1
        elif star >= 1:
            star -= 1
            t += 1
    if s == 0:
        if num >= 1:
            num -= 1
            s += 1
        elif star >= 1:
            star -= 1
            s += 1
print(sets)