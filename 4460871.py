NM = str(input())
N = int(NM[0])
M = int(NM[2])
ice = 0
for i in range(N):
    A = int(input())
    if A < M:
        ice += M - A
print(ice)