lines1 = input().split()
lines2 = input().split()
N = int(lines1[0])
M = int(lines1[1])
trees = []
for i in range(N):
    trees.append(int(lines2[i]))
trees.sort()
H = trees[N-1]
wood = 0
while wood < M:
    wood = 0
    for i in range(N):
        temp = trees[i] - H
        if temp < 0:
            temp = 0
        wood += temp
    if wood < M:
        H -= 1
print(H)