n = int(input())
f = 0
if n >= 20:
    n = n/20
    f += n+1
if n == 0 or n == 4 or n == 5 or n == 8 or n == 9 or n == 10 or n == 12 or n == 13 or n == 14 or n == 15 or n == 16 or n == 17 or n == 18:
    f += 1
print(int(f))