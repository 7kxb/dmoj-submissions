x = y
temp0[-]
x[-]
y[x+temp0+y-]
temp0[y+temp0-]

x = x + y
Wrapping
temp0[-]
y[x+temp0+y-]
temp0[y+temp0-]
y[-x+y]x

x = x - y
Wrapping
temp0[-]
y[x-temp0+y-]
temp0[y+temp0-]

x = x * y
temp0[-]
temp1[-]
x[temp1+x-]
temp1[
 y[x+temp0+y-]temp0[y+temp0-]
temp1-]

x = x * x
x[temp0+x-]
temp0[-[temp1+x++temp0-]x+temp1[temp0+temp1-]temp0]

x = x / y
temp0[-]
temp1[-]
temp2[-]
temp3[-]
x[temp0+x-]
temp0[
 y[temp1+temp2+y-]
 temp2[y+temp2-]
 temp1[
  temp2+
  temp0-[temp2[-]temp3+temp0-]
  temp3[temp0+temp3-]
  temp2[
   temp1-
   [x-temp1[-]]+
  temp2-]
 temp1-]
 x+
temp0]
x[
 temp1+[
  y[x-[temp1+†]temp1-temp0+y-]
  temp0[y+temp0-]q+temp1
 ]
]
x[y[temp0+x+y-]temp0[y+temp0-]q-†]

x = x ^ y
 temp0[-]
 x[temp0+x-]
 x+
 y[
   temp1[-]
   temp2[-]
   x[temp2+x-]
   temp2[
     temp0[x+temp1+temp0-]
     temp1[temp0+temp1-]
   temp2-]
 y-]

swap x, y
temp0[-]
x[temp0+x-]
y[x+y-]
temp0[y+temp0-]
Wrapping
Another algorithm:
x[-temp0+y-x]
y[-x+y]
temp0[-y+x+temp0]

x = -x
Wrapping
temp0[-]
x[temp0-x-]
temp0[x-temp0+]
Non-Wrapping
Requires another variable signx, where 0 = positive, 1 = negative.
temp0[-]+
signx[temp0-signx-]
temp0[signx+temp0-]