a = [0 for i in range(30000)]
b = ""
c = 0
while "#" not in b:
    b = input()
    for i in range(len(b)):
        if b[i] == ">":
            c += 1
            if c == 30000:
                c = 0
        elif b[i] == "<":
            c -= 1
            if c == -1:
                c = 29999
        elif b[i] == "+":
            a[c] += 1
            if a[c] == 256:
                a[c] = 0
        elif b[i] == "-":
            a[c] -= 1
            if a[c] == 0:
                a[c] = 255
        elif b[i] == "[":
            if a[c] == 0:
                while b[i] != "]":
                    c += 1
        elif b[i] == "]":
            if a[c] != 0:
                while b[i] != "[":
                    c -= 1
        elif b[i] == ".":
            print(chr(a[c]))