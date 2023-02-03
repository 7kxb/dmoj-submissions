tiles14 = str(input()).split(' ')
tiles58 = str(input()).split(' ')
tiles912 = str(input()).split(' ')
tiles1316 = str(input()).split(' ')

tile1 = tiles14[0]
tile2 = tiles14[1]
tile3 = tiles14[2]
tile4 = tiles14[3]
tile5 = tiles58[0]
tile6 = tiles58[1]
tile7 = tiles58[2]
tile8 = tiles58[3]
tile9 = tiles912[0]
tile10 = tiles912[1]
tile11 = tiles912[2]
tile12 = tiles912[3]
tile13 = tiles1316[0]
tile14 = tiles1316[1]
tile15 = tiles1316[2]
tile16 = tiles1316[3]

A = tile1 + tile2 + tile3 + tile4
B = tile1 + tile5 + tile9 + tile13
C = tile4 + tile8 + tile12 + tile16
D = tile13 + tile14 + tile15 + tile16
E = tile2 + tile6 + tile10 + tile14
F = tile3 + tile7 + tile11 + tile15
G = tile5 + tile6 + tile7 + tile8
H = tile9 + tile10 + tile11 + tile12

if A+B+C+D+E+F+G+H == A*8:
    print('magic')
else:
    print('not magic')