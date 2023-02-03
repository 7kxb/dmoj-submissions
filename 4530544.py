tiles14 = str(input()).split(' ')
tiles58 = str(input()).split(' ')
tiles912 = str(input()).split(' ')
tiles1316 = str(input()).split(' ')

tile1 = int(tiles14[0])
tile2 = int(tiles14[1])
tile3 = int(tiles14[2])
tile4 = int(tiles14[3])
tile5 = int(tiles58[0])
tile6 = int(tiles58[1])
tile7 = int(tiles58[2])
tile8 = int(tiles58[3])
tile9 = int(tiles912[0])
tile10 = int(tiles912[1])
tile11 = int(tiles912[2])
tile12 = int(tiles912[3])
tile13 = int(tiles1316[0])
tile14 = int(tiles1316[1])
tile15 = int(tiles1316[2])
tile16 = int(tiles1316[3])

A = tile1 + tile2 + tile3 + tile4
B = tile1 + tile5 + tile9 + tile13
C = tile4 + tile8 + tile12 + tile16
D = tile13 + tile14 + tile15 + tile16
E = tile2 + tile6 + tile10 + tile14
F = tile3 + tile7 + tile11 + tile15
G = tile5 + tile6 + tile7 + tile8
H = tile9 + tile10 + tile11 + tile12

if A == B:
    if B == C:
        if C == D:
            if D == E:
                if E == F:
                    if F == G:
                        if G == H:
                            print('magic')
                        else:
                            print('not magic')
                    else:
                        print('not magic')
                else:
                    print('not magic')
            else:
                print('not magic')
        else:
            print('not magic')
    else:
        print('not magic')
else:
    print('not magic')