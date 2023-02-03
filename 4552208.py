number = int(input())
string = str(input())
A = 0
B = 0
for i in range(number):
    if 'A' in string[i]:
        A += 1
    if 'B' in string[i]:
        B += 1
if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')