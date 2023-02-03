temp = open(False).read()
var1 = []
for x in range(26):
    up = temp.count(chr(i+97))
    down = temp.count(chr(i+65))
    var2 = up + down
    var1.append(str(var2))
print(' '.join(var1))