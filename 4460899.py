NM = str(input())
B = NM.index(' ')
N = int(NM[0:B])
M = int(NM[B:])
ice = 0
for i in range(N):
    A = int(input())
    if A < M:
        ice += M - A
print(ice)