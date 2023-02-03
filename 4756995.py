for i in range(5):
    dict = {1:56,2:320,3:1624,4:7152,5:26016,6:72912,7:140704,8:140704,9:140704}
    n = int(input())
    a = 0
    for i in range(1,n+1):
        a += dict.get(i)
    print(a)