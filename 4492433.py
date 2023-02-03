import sys
all_data = sys.stdin.read().split('\n')
A = int(alldata[0]) + int(alldata[1]) + int(alldata[2])
B = A % 42069900169420
print(B)