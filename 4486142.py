L = int(input())
M = int(input())
N = int(input())

if L < M and L > N:
    print(L)

if L > N and L < M:
    print(L)
    
if N < M and N > L:
    print(N)

if N > L and N < M:
    print(N)
    
if M < L and M > N:
    print(M)

if N > N and N < L:
    print(M)