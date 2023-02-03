quarters = int(input())
a = int(input())
b = int(input())
c = int(input())

counter = 0

while quarters > 0:
    playA()
    playB()
    playC()
    
if quarters == 0:
    print('Martha plays ' + counter + ' times before going broke.')
    
def playA():
    a += 1
    counter += 1
    quarters -= 1
    if a == 35:
        quarters += 30

def playB():
    b += 1
    counter += 1 
    quarters -= 1 
    if b == 100:
        quarter += 60
        
def playC():
    c += 1 
    counter += 1
    quarters -= 1
    if c == 10:
        quarters += 9