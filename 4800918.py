for _ in range(5):
    a = [[0 for i in range(13)]for i in range(9)]
    b = input()
    for i in range(len(b)):
        c = 5
        j = i
        q = False
        r = False
        s = False
        t = False
        u = False
        v = False
        w = False
        x = False
        y = False
        z = False
        while j == i:
            if a[c][int(b[i])+2] == 0:
                if i%2 == 0:
                    a[c][int(b[i])+2] = 1
                    j = -1
                    if a[c][int(b[i])-1] == 1 and a[c][int(b[i])] == 1 and a[c][int(b[i])+1] == 1:
                        q = True
                    if q:
                        print('RED-'+str(i+1))
                    if a[c+1][int(b[i])-1] == 1 and a[c+2][int(b[i])] == 1 and a[c+3][int(b[i])+1] == 1:
                        r = True
                    if r:
                        print('RED-'+str(i+1))
                    if a[c+1][int(b[i])+3] == 1 and a[c+2][int(b[i])+4] == 1 and a[c+3][int(b[i])+5] == 1:
                        s = True
                    if s:
                        print('RED-'+str(i+1))
                    if a[c][int(b[i])+3] == 1 and a[c][int(b[i])+4] == 1 and a[c][int(b[i])+5] == 1:
                        t = True
                    if t:
                        print('RED-'+str(i+1))
                    if a[c+1][int(b[i])+2] == 1 and a[c+2][int(b[i])+2] == 1 and a[c+3][int(b[i])+2] == 1:
                        u = True 
                    if u:
                        print('RED-'+str(i+1))
                elif i%2 == 1:
                    a[c][int(b[i])+2] = 2
                    j = -1
                    if a[c][int(b[i])-1] == 2 and a[c][int(b[i])] == 2 and a[c][int(b[i])+1] == 2:
                        v = True
                    if v:
                        print('BLUE-'+str(i+1))
                    if a[c+1][int(b[i])-1] == 2 and a[c+2][int(b[i])] == 2 and a[c+3][int(b[i])+1] == 2:
                        w = True
                    if w:
                        print('BLUE-'+str(i+1))
                    if a[c+1][int(b[i])+3] == 2 and a[c+2][int(b[i])+4] == 2 and a[c+3][int(b[i])+5] == 2:
                        x = True
                    if x:
                        print('BLUE-'+str(i+1))
                    if a[c][int(b[i])+3] == 2 and a[c][int(b[i])+4] == 2 and a[c][int(b[i])+5] == 2:
                        y = True
                    if y:
                        print('BLUE-'+str(i+1))
                    if a[c+1][int(b[i])+2] == 2 and a[c+2][int(b[i])+2] == 2 and a[c+3][int(b[i])+2] == 2:
                        z = True 
                    if z:
                        print('RED-'+str(i+1))
            else:
                c -= 1