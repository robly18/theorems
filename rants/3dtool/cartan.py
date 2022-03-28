import numpy.matlib as np
import math

from itertools import chain

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

def f(t):
    return np.array([t, - 0.15 * math.sin(t*4)-0.2*t])

v = np.array([0.3,0.5])

tt = np.linspace(-1,1,20)

glops="draw=none, fill=orange"
print(drawPath(chain((f(t) for t in tt), (f(t)-v for t in reversed(tt)))))

glops="red, thick"
print(drawPlot(f(t) for t in tt))

glops="blue, thick"
print(drawPlot(f(t)-v for t in tt))

glops = "->,thick"
for t in np.linspace(-1,1,4):
    print(drawPath([f(t)-v,f(t)]))

