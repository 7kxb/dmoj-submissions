N = str(input())
k = int(input())

total = int(N)

for i in range(k):
    N = N + '0'
    total += int(N)
    
print(total)