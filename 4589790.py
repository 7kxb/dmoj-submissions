h = int(input())
m = int(input())
for i in range(m):
    t = i+1
    a = -6*t**4 + h*t**3 + 2*t**2 + t
    if a <= 0:
        print('The balloon first touches ground at hour:\n'+str(t))
        break
if a > 0:
    print('The balloon does not touch ground in the given time.')