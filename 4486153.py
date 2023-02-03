L = int(input())
M = int(input())
N = int(input())

if L < M and L > N:
    print(L)

elif L > M and L < N:
    print(L)
    
elif N < M and N > L:
    print(N)

elif N > M and N < L:
    print(N)
    
elif M < L and M > N:
    print(M)

elif M > L and M < N:
    print(M)