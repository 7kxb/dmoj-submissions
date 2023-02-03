n = int(input())
for _ in range(n):
    test_list = input()
    check_str = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ra', 'ri', 'ru', 're', 'ro']
    temp = '\t'.join(test_list)
    for i in range(len(check_str)):
        res = any(check_str[i] in sub for sub in test_list)
        if res == True:
            print('YES')
            break
    if not res:
        print('NO')