l,h,w = map(int, input().split())
d = int(input())
vr = l*w*h
vc = 3.14*((d/2)**2)*h
print(round(vr - vc, 2))