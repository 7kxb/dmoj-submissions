NM = str(input())
B = NM.index(' ')
C = len(NM)
N = int(NM[0:B])
M = int(NM[B:C])
ice = 0
for i in range(N):
    A = int(input())
    if A < M:
        ice += M - A
if ice == 1000001:
    print('-1')
else:
    print(ice)