temp = input().split()
row = int(temp[0]) 
col = int(temp[1])
cat = int(input())
list1 = []
list2 = []
for i in range(row+1):
    row1 = []
    row2 = []
    for j in range(col+1):
        row1.append(0)
        row2.append(False)
    list1.append(row1)
    list2.append(row2)
for i in range(cat):
    temp = input().split()
    cat_row = int(temp[0])
    cat_col = int(temp[1])
    list1[cat_row][cat_col] = 0
    list2[cat_row][cat_col] = True
list1[1][1] = 1
list2[1][1] = True
for i in range(row+1):
    for j in range (col+1):
        if not list2[i][j]:
            list1[i][j] = list1[i-1][j] + list1[i][j-1]
print(list1[row][col])