limit = int(input())
speed = int(input())

if speed <= limit:
    print('Congratulations, you are within the speed limit!')
elif speed >= limit+31:
    print('You are speeding and your fine is $500.')
elif speed >= limit+21:
    print('You are speeding and your fine is $270.')
elif speed >= limit+1:
    print('You are speeding and your fine is $100.')