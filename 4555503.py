year = str(input())

a1 = 0 
b2 = 0 
c3 = 0 
d4 = 0 
e5 = 0 

if len(year) == 1:
    print(int(year)+1)

if len(year) == 2:
    c3 = -1
    d4 = int(year[0])
    e5 = int(year[1])
    e5 += 1
    if e5 == 10:
        e5 = 0
        d4 += 1
        if d4 == 10:
            d4 = 0
            if c3 == -1:
                c3 += 2
            else:
                c3 += 1
            if c3 == 10:
                c3 = 0 
                b2 += 1
                if b2 == 10:
                    b2 = 0
                    a1 += 1
    while d4 == e5 or c3 == d4 or c3 == e5:
        e5 += 1
        if e5 == 10:
            e5 = 0
            d4 += 1
            if d4 == 10:
                d4 = 0
                if c3 == -1:
                    c3 += 2
                else:
                    c3 += 1
                if c3 == 10:
                    c3 = 0 
                    b2 += 1
                    if b2 == 10:
                        b2 = 0
                        a1 += 1
    if c3 == -1:
        print(str(d4)+str(e5))
    else:
        print(str(c3)+str(d4)+str(e5))

if len(year) == 3:
    b2 = -1
    c3 = int(year[0])
    d4 = int(year[1])
    e5 = int(year[2])
    e5 += 1
    if e5 == 10:
        e5 = 0
        d4 += 1
        if d4 == 10:
            d4 = 0
            c3 += 1
            if c3 == 10:
                c3 = 0 
                if b2 == -1:
                    b2 += 2
                else:
                    b2 += 1
                if b2 == 10:
                    b2 = 0
                    a1 += 1
    while d4 == e5 or c3 == d4 or c3 == e5 or b2 == c3 or b2 == d4 or b2 == e5:
        e5 += 1
        if e5 == 10:
            e5 = 0
            d4 += 1
            if d4 == 10:
                d4 = 0
                c3 += 1
                if c3 == 10:
                    c3 = 0 
                    if b2 == -1:
                        b2 += 2
                    else:
                        b2 += 1
                    if b2 == 10:
                        b2 = 0
                        a1 += 1
    if b2 == -1:
        print(str(c3)+str(d4)+str(e5))
    else:
        print(str(b2)+str(c3)+str(d4)+str(e5))

if len(year) == 4:
    a1 = -1
    b2 = int(year[0])
    c3 = int(year[1])
    d4 = int(year[2])
    e5 = int(year[3])
    e5 += 1
    if e5 == 10:
        e5 = 0
        d4 += 1
        if d4 == 10:
            d4 = 0
            c3 += 1
            if c3 == 10:
                c3 = 0 
                b2 += 1
                if b2 == 10:
                    b2 = 0
                    if a1 == -1:
                        a1 += 2
                    else:
                        a1 += 1
    while d4 == e5 or c3 == d4 or c3 == e5 or b2 == c3 or b2 == d4 or b2 == e5 or a1 == b2 or a1 == c3 or a1 == d4 or a1 == e5:
        e5 += 1
        if e5 == 10:
            e5 = 0
            d4 += 1
            if d4 == 10:
                d4 = 0
                c3 += 1
                if c3 == 10:
                    c3 = 0 
                    b2 += 1
                    if b2 == 10:
                        b2 = 0
                        if a1 == -1:
                            a1 += 2
                        else:
                            a1 += 1
    if a1 == -1:
        print(str(b2)+str(c3)+str(d4)+str(e5))
    else:
        print(str(a1)+str(b2)+str(c3)+str(d4)+str(e5))

if len(year) == 5:
    print('10234')