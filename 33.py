import math

def distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

ax=int(input())
ay=int(input())
bx=int(input())
by=int(input())
cx=int(input())
cy=int(input())
perimeter=distance(ax,ay,bx,by)+distance(cx,cy,ax,ay)+distance(bx,by,cx,cy)
print(perimeter)
