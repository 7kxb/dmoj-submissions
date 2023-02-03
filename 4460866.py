NM = input()
ice = 0
for i in range(int(NM[0])):
    A = input()
    if A < M:
        ice += int(NM[2]) - int(A)
print(ice)