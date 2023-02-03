v = ['a','e','i','o','u']
c = ['k','n','h','f','m','r']
b = ['b','c','d','g','j','l','p','q','s','t','v','w','x','y','z']
n = int(input())
def check(a,v,c,b):
    j = 0
    while j != len(a):
        if a[j] in b:
            return 'NO'
        if a[j] in v:
            j += 1
        if j == len(a):
            return 'YES'
        if a[j] in c:
            if j + 1 != len(a):
                if a[j+1] in v:
                    j += 2
                else:
                    return 'NO'
            else:
                return 'NO'
        if j == len(a):
            return 'YES'
for i in range(n):
    a = input()
    print(check(a,v,c,b))