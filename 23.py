import math
x= int(input())
y= int(input())
z= int(input())
a=(2*math.cos(x-(math.pi/6)))/((1/2)+math.sin(y)**2)
b=1+((z**2)/(3+((z**2)/5)))
print(a,b)