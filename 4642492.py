M = int(input())
N = int(input())
K = int(input())
array = []
for i in range(M):
     row = []
     for i in range(N):
         row.append('B')
     array.append(row)
for i in range(K):
     temp = input()
     R1 = 0
     R2 = 0
     R3 = 0
     C1 = 0
     C2 = 0
     C3 = 0
     if temp == 'R 1':
         R1 += 1
     if temp == 'R 2':
         R2 += 1
     if temp == 'R 3':
         R3 += 1
     if temp == 'C 1':
         C1 += 1
     if temp == 'C 2':
         C2 += 1
     if temp == 'C 3':
         C3 += 1
if R1%2 == 1:
    for i in range(N):
        array[int(1)-1][i] == 'G'
if R2%2 == 1:
    for i in range(N):
        array[int(2)-1][i] == 'G'
if R3%2 == 1:
    for i in range(N):
        array[int(3)-1][i] == 'G'
if C1%2 == 1:
    for i in range(M):
        array[i][int(1)-1] == 'G'
if C2%2 == 1:
    for i in range(M):
        array[i][int(2)-1] == 'G'
if C3%2 == 1:
    for i in range(M):
        array[i][int(3)-1] == 'G'
gold = 0
for h in range(M):
     for i in range(N):
         if array[h][i] == 'B':
             gold += 0
         if array[h][i] == 'G':
             gold += 1
print(gold)