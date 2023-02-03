n = int(input())
s = input()
def chk(n, s):
    fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    for i in range(n):
        if s[i] == 'A':
            if i+1 == fib[0]:
                fib.pop(0)
            else:
                return 'Bruno, GO TO SLEEP'
        elif s[i] != 'A':
            if i+1 == fib[0]:
                return 'Bruno, GO TO SLEEP'
    return "That's quite the observation!"
print(chk(n,s))