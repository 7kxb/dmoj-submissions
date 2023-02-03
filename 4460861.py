NM = input()
ice = 0
for i in range(int(NM[0])):
    A = int(input())
    if A < M:
        ice += int(NM[1]) - A
print(ice)