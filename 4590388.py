n = int(input())
for i in range(n):

    a = input().lower()
    b = []
    c = True
    
    if 'a' in a:
        d = 0
    else:
        b.append('a')
        c = False
        
    if 'b' in a:
        d = 0
    else:
        b.append('b')
        c = False
    
    if 'c' in a:
        d = 0
    else:
        b.append('c')
        c = False
        
    if 'd' in a:
        d = 0
    else:
        b.append('d')
        c = False
        
    if 'e' in a:
        d = 0
    else:
        b.append('e')
        c = False
    
    if 'f' in a:
        d = 0
    else:
        b.append('f')
        c = False
    
    if 'g' in a:
        d = 0
    else:
        b.append('g')
        c = False
        
    if 'h' in a:
        d = 0
    else:
        b.append('h')
        c = False
        
    if 'i' in a:
        d = 0
    else:
        b.append('i')
        c = False
    
    if 'j' in a:
        d = 0
    else:
        b.append('j')
        c = False
        
    if 'k' in a:
        d = 0
    else:
        b.append('k')
        c = False
        
    if 'l' in a:
        d = 0
    else:
        b.append('l')
        c = False
    
    if 'm' in a:
        d = 0
    else:
        b.append('m')
        c = False
        
    if 'n' in a:
        d = 0
    else:
        b.append('n')
        c = False
        
    if 'o' in a:
        d = 0
    else:
        b.append('o')
        c = False
        
    if 'p' in a:
        d = 0
    else:
        b.append('p')
        c = False
        
    if 'q' in a:
        d = 0
    else:
        b.append('q')
        c = False
        
    if 'r' in a:
        d = 0
    else:
        b.append('r')
        c = False
    
    if 's' in a:
        d = 0
    else:
        b.append('s')
        c = False
    
    if 't' in a:
        d = 0
    else:
        b.append('t')
        c = False
        
    if 'u' in a:
        d = 0
    else:
        b.append('u')
        c = False
        
    if 'v' in a:
        d = 0
    else:
        b.append('v')
        c = False
        
    if 'w' in a:
        d = 0
    else:
        b.append('w')
        c = False
        
    if 'x' in a:
        d = 0
    else:
        b.append('x')
        c = False
        
    if 'y' in a:
        d = 0
    else:
        b.append('y')
        c = False
        
    if 'z' in a:
        d = 0
    else:
        b.append('z')
        c = False
        
    if c:
        print('pangram')
    else:
        e = ''
        for f in range(len(b)):
            e += b[f]
        print('missing',e)