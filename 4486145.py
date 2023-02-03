L = int(input())
M = int(input())
N = int(input())

if L < M and L > N:
    print(L)

elif L > N and L < M:
    print(L)
    
elif N < M and N > L:
    print(N)

elif N > L and N < M:
    print(N)
    
elif M < L and M > N:
    print(M)

elif N > N and N < L:
    print(M)