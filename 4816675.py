n = int(input())
l = list(map(int,input().split()))
print(['NO', 'YES'][len(set(l)) == n])