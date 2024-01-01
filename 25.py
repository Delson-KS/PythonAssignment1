import math
x=int(input())
y=int(input())
z=int(input())
a=math.log((y-math.sqrt(abs(x)))*(x-(y/(z+((x**2)/4)))))
b=x-((x**2)/math.factorial(3))+((x**5)/math.factorial(5))
print(a,b)