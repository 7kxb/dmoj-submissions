lines = int(input())
for _ in range(lines):
    string = input().split()
    length = len(string)
    for i in range(length):
        if len(string[i]) == 4:
            string[i] = '****'
    text = ''
    for i in range(length):
        if i == 0:
            text += string[i]
        else:
            text += ' ' + string[i]
    print(text)