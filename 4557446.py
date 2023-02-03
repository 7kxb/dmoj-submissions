M = int(input())
N = int(input())
K = int(input())
array = []
for i in range(M):
     row = []
     for i in range(N):
         row.append(-1)
     array.append(row)
for i in range(K):
     temp = input()
     temp2 = temp.split()
     if temp[0] == 'R':
         for i in range(N):
             array[int(temp2[1])-1][i] *= -1
     if temp[0] == 'C':
         for h in range(M):
             array[h][int(temp2[1])-1] *= -1
art = ''
for h in range(M):
     for i in range(N):
         if array[h][i] == -1:
             art += 'B'
         if array[h][i] == 1:
             art += 'G'
gold = 0
for j in range(M*N):
     if art[j] == 'G':
         gold += 1 
print(gold)