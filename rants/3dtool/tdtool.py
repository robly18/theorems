import numpy.matlib as np
import math

sq2 = math.sqrt(2)

def projMatrix(alpha, h):
    ch = math.sqrt(1 - h**2)
    return np.mat(
        [[math.cos(alpha), math.sin(alpha), 0],
         [-math.sin(alpha)*ch, math.cos(alpha)*ch, h]])

pm = projMatrix(math.pi * 0.6, .9)

def showPair(mat):
    return "({:.3f},{:.3f})".format(mat[0,0],mat[0,1])

def go3dto2d(pt):
    return pm.dot(pt)

def showPt(pt):
    if type(pt) is str:
        return pt
    return showPair(go3dto2d(pt))

glops = ""
def drawPath(points, options=None):
    if options is None:
        options = glops
    return "\\draw[{}] {}; ".format(options,"--".join(map(showPt, points)))
def drawPoint(pt, options=None):
    if options is None:
        options = glops
    return "\\node[{}] at {} {{}}; ".format(options,showPt(pt))

glops = "->"
print(drawPath([(0,0,0),(3,0,0)]))
print(drawPath([(0,0,0),(0,5,0)]))
print(drawPath([(0,0,0),(0,0,5)]))

r2 = 7.1**2

def surface(x,y):
    return np.array((
            x,y,
            math.sqrt(r2-x**2-y**2) - 5 if x**2+y**2 <= r2 else 0
            ))

#todo set x0, y0, and make plot of tangent to surface at that point
x0 = 1
y0 = 1.5
pc = np.array([x0,y0])
p = surface(x0,y0)

def tangent(x,y):
    return p + (x-x0, y-y0,
            - (x0*(x-x0) + y0*(y-y0))/math.sqrt(r2-x0**2-y0**2))

glops = "gray"
for x in np.linspace(0,3,7):
    print(drawPath([surface(x,y) for y in np.linspace(0,4,11)]))
for y in np.linspace(0,4,9):
    print(drawPath([surface(x,y) for x in np.linspace(0,3,11)]))

glops = "blue"
for x in np.linspace(x0-1,x0+1,5):
    print(drawPath([tangent(x,y) for y in np.linspace(y0-1,y0+1,2)]))
for y in np.linspace(y0-1,y0+1,5):
    print(drawPath([tangent(x,y) for x in np.linspace(x0-1,x0+1,2)]))

v1 = np.array([-1,0])
v2 = np.array([.5,-1])
eps = .25

glops = "fill=orange"
print(drawPath([p, tangent(*(pc+v1*eps)),
                tangent(*(pc+v2*eps+v1*eps)), tangent(*(pc+v2*eps)), "cycle"]))
glops = "->,thick"
print(drawPath([p, tangent(*(pc+v1))]))
print(drawPath([p, tangent(*(pc+v2))]))

print(drawPoint(p, "circle,draw,fill=red,inner sep=2pt"))