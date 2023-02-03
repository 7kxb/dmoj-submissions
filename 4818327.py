vowels = ['a', 'e', 'i', 'o', 'u', 'y']
n,c,v = map(int,input().split())
a = input()
def check(n,c,v,a):
    c1 = 0
    v1 = 0
    for i in range(n):
        if a[i] == 'y':
            c1 += 1 
            v1 += 1
        elif a[i] in vowels:
            v1 += 1
            c1 = 0
        else:
            c1 += 1
            v1 = 0
        if c1 == c or v1 == v:
            return 'NO'
    return 'YES'
print(check(n,c,v,a))