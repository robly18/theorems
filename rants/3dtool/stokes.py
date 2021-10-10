import numpy.matlib as np
import math


def showPair(p):
    return "({:.3f},{:.3f})".format(p[0],p[1])

def showPt(pt):
    if type(pt) is str:
        return pt
    return showPair(pt)

glops = ""
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

def distort(p):
    (x,y) = p
    (x2,y2) = (x-math.sin(y+.1)*.2,y+math.exp(-x**2)) #change as needed
    a = -.2
    return (math.cos(a) * x2 + math.sin(a) * y2 + 2, -math.sin(a) * x2 + math.cos(a) * y2 + 1.6)

N = 30

circle = [(math.cos(t), math.sin(t)) for t in np.linspace(0, 2*math.pi, num=N, endpoint=False)]
startpoints = [(-.3, -.3), (.2, -1.3), (-1.2,.7)]

def flow(p0):
    (x,y) = p0
    return [(xx, y) for xx in np.linspace(x, 3 + .2*x, num=N)]

def nodes(p0):
    (x,y) = p0
    if abs(y) > 1:
        return
    minx = -math.sqrt(1 - y**2)
    maxx = -minx
    if x < minx:
        yield ((minx, y), "blue")
    if x < maxx:
        yield ((maxx, y), "red")

print(drawPlot(map(distort,circle), cycle=True))

glops="red,->"

for p in startpoints:
    print(drawPath(map(distort,flow(p))))
    for n,c in nodes(p):
        print(drawPoint(distort(n), options="atom,fill={}".format(c)))
    print(drawPoint(distort(p), options="atom, inner sep=1.5pt"))
    print(drawPoint(distort(p), options="cross out, draw, inner sep=1.5pt"))


