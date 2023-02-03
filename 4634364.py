toggle = True
while toggle:
    N = input()
    if N != "quit!":
        x = len(N)
        if "or" in N: 
            if x > 4:
                N = N.replace("or","our")
        print(N)
    else:
        toggle = False