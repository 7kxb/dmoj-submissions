from datetime import datetime
str_d1 = input()
str_d2 = input()
d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")
delta = d2 - d1
print(delta.days)