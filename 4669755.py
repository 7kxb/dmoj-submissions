n = int(input())
o = n-1
p = o-1
print('#'*o+'.')
for i in range(p):
    print('#'+'.'*p+'#')
print('#'*o+'.')
for i in range(o):
    r = p-i
    print('#'+'.'*i+'#'+'.'*r)