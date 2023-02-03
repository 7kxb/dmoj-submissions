from operator import xor
for i in range(int(input())):
  s,f = map(int,input().split())
  a = 0
  for i in range(s,f+1):
    a = xor(a,i)
  print(a)