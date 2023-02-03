amount = int(input())
string = input()
list1 = string.split()
print(string)

for i in range(0,len(list1)-1):  
        for j in range(len(list1)-i-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp
                counter = 0
                output = ''
                for k in range(amount):
                    if counter != 0:
                        output = output + ' ' + str(list1[counter])
                    else:
                        output = output + str(list1[counter])
                    counter += 1
                print(output)