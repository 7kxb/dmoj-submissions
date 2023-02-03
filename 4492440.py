import sys
A = sys.stdin.read().split('\n')
B = int(A[0])
C = int(A[2])
D = int(A[4])
E = B + C + D
F = E % 42069900169420
print(F)