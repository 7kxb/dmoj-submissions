words = int(input())
count = 0
for i in range(words):
    word = input()
    temp = len(word)
    prog = 0
    for j in range(temp):
        if word[j] == 'q' or word[j] == 'w' or word[j] == 'e' or word[j] == 'r' or word[j] == 't' or word[j] == 'y' or word[j] == 'u' or word[j] == 'i' or word[j] == 'o' or word[j] == 'p':
            prog += 1
        if prog == temp:
            count += 1
    prog = 0
    for j in range(temp):
        if word[j] == 'a' or word[j] == 's' or word[j] == 'd' or word[j] == 'f' or word[j] == 'g' or word[j] == 'h' or word[j] == 'j' or word[j] == 'k' or word[j] == 'l':
            prog += 1 
        if prog == temp:
            count += 1
    prog = 0
    for j in range(temp):
        if word[j] == 'z' or word[j] == 'x' or word[j] == 'c' or word[j] == 'v' or word[j] == 'b' or word[j] == 'n' or word[j] == 'm':
            prog += 1
        if prog == temp:
            count += 1
print(count)