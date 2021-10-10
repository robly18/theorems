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

glops="red,->"

for x in [.5,1.5,2.5]:
    for y in np.arange(-3,4):
        print(drawPath([(x,y+x*.1-.1),(3.2,y+x*.1-.1)], "red,->, thick"))
        #print(drawPoint((x,y+x*.1-.1), "atom"))
        print(drawPath([(-3.2,y-x*.1+.1),(-x,y-x*.1+.1)], "blue,->, thick"))
        #print(drawPoint((-x,y-x*.1+.1), "atom"))