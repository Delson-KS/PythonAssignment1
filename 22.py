import math
x=int(input())
y=int(input())
z=int(input())
a=y+(x/((y**2)+abs(((x**2)/y+((x*3)/3)))))
b=1+(math.tan(z/2)**2)
print(a,b)