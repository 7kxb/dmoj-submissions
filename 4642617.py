n = int(input())
for i in range(1,int(n/2+.5)+1):
    j = 2*i-1
    k = 2*n-j*2
    print('*'*j + ' '*k + '*'*j)
for i in range(int(n/2),0, -1):
    j = 2*i-1
    k = 2*n-j*2
    print('*'*j + ' '*k + '*'*j)