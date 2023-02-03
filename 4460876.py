NM = input()
N = int(NM[0])
M = int(NM[2])
ice = 0
for i in range(N):
    A = input()
    if A < M:
        ice += M - int(A)
print(ice)