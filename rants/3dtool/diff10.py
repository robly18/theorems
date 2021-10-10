from tdtool import *
import math
setPM(math.pi*.03,.995)

R = 4



def param(r, t, sign):
    #parametrizes the curve xy = r (the positive part if sign=1)
    #as a function of t = (x-y)/2
    #this for positive r. for negatives, use t = (x+y)/2
    if r > 0:
        s = math.sqrt(t**2 + r)
        return (sign*(s+t),sign*(s-t))
    else:
        s = math.sqrt(t**2 - r)
        return (sign*(t+s),sign*(t-s))

def bound(r):
    #returns b, where t in [-b,b] parametrizes the curve xy = r inside the square of radius R = 3
    if r > 0:
        return (R-r/R)/2
    else:
        return (R+r/R)/2

def surface(p,h):
    (x,y) = p
    return (x,y,h)

def drawHyperbole(r, h, sign):
    points = [surface(param(r,t,sign), h) for t in np.linspace(-bound(r),bound(r),20)]
    color = ""
    arrow = ""
    if r > 0:
        color="red"
        arrow="->"
    else:
        color="blue"
        arrow="<-"
    opts="color={},{}".format(color,arrow)
    return drawPath(points, opts)



rset = [.5 + 2*i for i in range(0,4)]

setglops("->")

for h in [0,1,2]:
    for r in rset:
        print(drawHyperbole(-r,h,-1))

for h in [0,1,2]:
    for r in rset:
        print(drawHyperbole(r,h,-1))
        print(drawHyperbole(r,h,1))



print(drawPath([(-R,0,0),(R,0,0)]))
print(drawPath([(0,-R,0),(0,R,0)]))
print(drawPath([(0,0,0),(0,0,3)]))
setglops("")

for h in [0,1,2]:
    for r in rset:
        print(drawHyperbole(-r,h,1))

