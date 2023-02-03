map = {1:1, 2:1}
def fib(n):
    if n in map:
        return map.get(n)
    elif n % 2 == 0:
        map[n] = fib(int(n/2)) * (2*fib((int(n/2))+1) - fib(int(n/2)))
        return map.get(n)
    map[n] = int(fib(((n-1)/2)+1)**2 + fib(int(n-1)/2)**2)
    return map.get(n)
n = int(input())
print(fib(n)%1000000007)