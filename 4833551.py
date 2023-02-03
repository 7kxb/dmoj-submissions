s = input()
a = False
for i in range(5):
    if input() == s:
        print('Y')
        a = True
if not a:
    print('N')