amount = int(input())
string = input()
list1 = string.split()
counter = 0
for i in range(0,len(list1)-1):  
        for j in range(len(list1)-i-1):  
            if(list1[j]<list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp
                counter += 1 
print(counter)