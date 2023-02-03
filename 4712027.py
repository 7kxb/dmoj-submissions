counter = 0
word = input()
for i in range(5):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or word[i] == 'y':
        counter += 1
if counter >= 2:
    print('good')
else:
    print('bad')