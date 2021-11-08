import numpy.matlib as np
import math


def showPair(p):
    return "({:.3f},{:.3f})".format(p[0],p[1])

def showPt(pt):
    if type(pt) is str:
        return pt
    return showPair(pt)

glops = ""
def drawNode(points, options=None):
    if options is None:
        options = glops
    return "\\draw[{}] {}; ".format(options,"--".join(map(showPt, points)))
def drawPoint(pt, options=None):
    if options is None:
        options = glops
    return "\\node[{}] at {} {{}}; ".format(options,showPt(pt))
def drawPath(pt, options=None):
    if options is None:
        options = glops
    return "\\draw[{}] {};".format(options, "--".join(map(showPt, pt)))
def drawPlot(points, options=None, **kwargs):
    if options is None:
        options = glops
    smooth = "smooth"
    if "cycle" in kwargs and kwargs["cycle"]:
        smooth+=" cycle"
    return "\\draw[{}] plot[{}] coordinates{{{}}}; ".format(options, smooth, " ".join(map(showPt, points)))

def f(x,y):
    return (math.sin(x)**2 + .1 * y**2, y)

def lsy(x,c):
    q = -math.sin(x)**2 + c
    assert(q > -.001)
    if q <= 0:
        return 0
    return math.sqrt(10*(-math.sin(x)**2 + c))

def dom(c):
    s = math.asin(math.sqrt(c))
    return (-s,s)

def curve(c, offset):
    if c <= 0:
        return None
    if c <= 1:
        (a,b) = dom(c)
        (a1, b1) = (a+offset, b+offset)
        cur = []
        for x in np.arange(a1, b1, .1):
            cur.append((x,lsy(x,c)))
        for x in np.arange(b1, a1, -.1):
            cur.append((x,-lsy(x,c)))
        return cur
    else:
        return [(x,lsy(x,c)*offset) for x in np.linspace(-3,3,15)]
            

glops="red, thick"

for c in [1/3,2/3,1]:
    print(drawPlot(curve(c,0),cycle=True))
    print(drawPlot(curve(c,math.pi),cycle=True))
    print(drawPlot(curve(c,-math.pi),cycle=True))
for c in [1.333333,1.666666]:
    print(drawPlot(curve(c,1)))
    print(drawPlot(curve(c,-1)))

#draw the image of w

def w(t):
    return (t, 1+t)

glops="thick,orange,->"
print(drawPlot(f(*w(t)) for t in np.linspace(0,1,10)))
