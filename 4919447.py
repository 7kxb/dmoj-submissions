n = int(input())
a = list(map(int,input().split()))

def sub_lists(my_list):
    subs = [[]] 
    for sub in my_list:
        subs += [i + [sub] for i in subs]
    return subs
    
print(sub_lists(a))

# brb