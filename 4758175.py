for _ in range(5):
    n = int(input())
    a = []
    for i in range(n):
        b = input()
        a.append(b+'.')
    a.append('.'*n)
    def count(n,a):
        c = 0
        for i in range(n):
            for j in range(n):
                if a[i][j] == '#':
                    c += 1
                    def count2(n,a,i,j):
                        x = 0
                        for k in range(1,n//2+1):
                            z = k*2+1
                            if a[i+k][j-k:j+k+1] == '#'*z:
                                x += 1
                            else:
                                return(x)
                        return(x)
                    c += count2(n,a,i,j)
        return(c)
    print(count(n,a))