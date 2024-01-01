import math
x=int(input())
y=int(input())
z=int(input())
a=(3+(math.e**(y-1)))/(1+(x**2)*abs(y-math.tan(z)))
b=1+abs(y-x)+(((y-x)**2)/2)+((abs(y-x)**3)/3)
print(a,b)