n = int(input())
for i in range(n):
    a = int(input())
    if a < 1000:
        print('Newbie')
    elif a >= 1000 and a < 1500:
        print('Amateur')
    elif a >= 1500 and a < 2000:
        print('Expert')
    elif a >= 1500 and a < 1800:
        print('Candidate Master')
    elif a >= 1800 and a < 2200:
        print('Master')
    elif a >= 2200 and a < 3000:
        print('Grandmaster')
    elif a >= 3000 and a < 4000:
        print('Target')
    else:
        print('Rainbow Master')