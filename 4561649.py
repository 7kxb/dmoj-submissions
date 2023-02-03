lines = int(input())
temp = []
for i in range(lines):
    puzzle = input().split()
    string1 = puzzle[0]
    string2 = puzzle[1]
    while string1 != string2:
        if 'aa' in string1:
            string1 = string1.replace('aa','b')
            #
        elif 'bb' in string1:
            string1 = string1.replace('bb','c')
            #
        elif 'cc' in string1:
            string1 = string1.replace('cc','d')
            #
        elif 'dd' in string1:
            string1 = string1.replace('dd','e')
            #
        elif 'ee' in string1:
            string1 = string1.replace('ee','f')
            #
        elif 'ff' in string1:
            string1 = string1.replace('ff','g')
            #
        elif 'gg' in string1:
            string1 = string1.replace('gg','h')
            #
        elif 'hh' in string1:
            string1 = string1.replace('hh','i')
            #
        elif 'ii' in string1:
            string1 = string1.replace('ii','j')
            #
        elif 'jj' in string1:
            string1 = string1.replace('jj','k')
            #
        elif 'kk' in string1:
            string1 = string1.replace('kk','l')
            #
        elif 'll' in string1:
            string1 = string1.replace('ll','m')
            #
        elif 'mm' in string1:
            string1 = string1.replace('mm','n')
            #
        elif 'nn' in string1:
            string1 = string1.replace('nn','o')
            #
        elif 'oo' in string1:
            string1 = string1.replace('oo','p')
            #
        elif 'pp' in string1:
            string1 = string1.replace('pp','q')
            #
        elif 'qq' in string1:
            string1 = string1.replace('qq','r')
            #
        elif 'rr' in string1:
            string1 = string1.replace('rr','s')
            #
        elif 'ss' in string1:
            string1 = string1.replace('ss','t')
            #
        elif 'tt' in string1:
            string1 = string1.replace('tt','u')
            #
        elif 'uu' in string1:
            string1 = string1.replace('uu','v')
            #
        elif 'vv' in string1:
            string1 = string1.replace('vv','w')
            #
        elif 'ww' in string1:
            string1 = string1.replace('ww','x')
            #
        elif 'xx' in string1:
            string1 = string1.replace('xx','y')
            #
        elif 'yy' in string1:
            string1 = string1.replace('yy','z')
            #
        else:
            temp.append('NO')
            break
    if string1 == string2:
        temp.append('YES')
for i in range(lines):
    print(temp[i])