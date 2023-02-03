lp = ['1','Q','A','Z']
lr = ['2','W','S','X']
lm = ['3','E','D','C']
li = ['4','R','F','V','5','T','G','B']
ri = ['6','Y','H','N','7','U','J','M']
rm = ['8','I','K',',']
rr = ['9','O','L','.']
rp = ['0','P',';','/','-','[',"'",'=',']']
lp2 = 0
lr2 = 0
lm2 = 0
li2 = 0
ri2 = 0
rm2 = 0
rr2 = 0
rp2 = 0
a = input()
for i in range(len(a)):
    if a[i] in lp:
        lp2 += 1
    if a[i] in lr:
        lr2 += 1
    if a[i] in lm:
        lm2 += 1
    if a[i] in li:
        li2 += 1
    if a[i] in ri:
        ri2 += 1
    if a[i] in rm:
        rm2 += 1
    if a[i] in rr:
        rr2 += 1
    if a[i] in rp:
        rp2 += 1
print(lp2)
print(lr2)
print(lm2)
print(li2)
print(ri2)
print(rm2)
print(rr2)
print(rp2)