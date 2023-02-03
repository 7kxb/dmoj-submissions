# 2 functions/methods taken from outside sources

def FR(k): # from tutorialspoint
  d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
  a = 0
  n = len(k)
  for (i, c) in enumerate(k):
     if i < n - 1 and d[c] < d[k[i + 1]]:
        a -= d[c]
     else:
        a += d[c]
  return a

def TR(k): # from stackoverflow
    n = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M'}
    return (n[(k//1000)*1000] + n[((k-((k//1000)*1000))//100)*100] + n[((k-(((k-((k//1000)*1000))//100)*100)-(k//1000)*1000)//10)*10] + n[k%10])


a = int(input())
for i in range(a):
    z = input()
    b,c = map(str,z.split('+'))
    c = c[0:-1]
    d = FR(b)
    e = FR(c)
    f = d+e
    g = TR(f)
    if f > 1000:
        print(z+'CONCORDIA CUM VERITATE')
    else:
        print(z+str(g))