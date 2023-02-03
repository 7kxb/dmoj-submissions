friend = int(input())
round = int(input())

old = []
counter = 1
for i in range(friend):
    old.append(counter)
    counter += 1
    
for i in range(round):
    eliminate = int(input())
    new = []
    counter = 1 
    for i in range(len(old)):
        if counter % eliminate != 0:
            new.append(old[counter-1])
        counter += 1 
        
    old = []
    counter = 0
    for i in new:
        old.append(new[counter])
        counter += 1 

counter = 0
for i in old:
    print(old[counter])
    counter += 1