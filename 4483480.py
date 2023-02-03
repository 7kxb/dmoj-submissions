for i in range(int(input())):
    NM = str(input())
    B = NM.index(' ')
    C = len(NM)
    N = int(NM[0:B])
    M = int(NM[B:C])
    A = N+M
    print(A)