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
def drawPath(pt, options=None, cycle=False):
    if options is None:
        options = glops
    maybecycle = "--cycle" if cycle else ""
    return "\\draw[{}] {} {};".format(options, "--".join(map(showPt, pt)), maybecycle)

glops=""

def r1(t):
    return 1+0.8*math.sin((math.sin(t+math.pi/2)+1) )+0.2*math.cos(3*t+math.pi/2)
    
print(drawPath([(3.5+1.4*r1(t)*math.cos(t),5+1.4*r1(t) * math.sin(t)) for t in np.arange(0.,2*math.pi,0.1)], cycle=True))

def r2(t):
    return 1+0.8*math.sin((math.cos(t+math.pi/6)+1) )+0.2*math.cos(3*t+math.pi/6)

print(drawPath([(6+1.2*r2(t)*math.cos(t),4.8+1.6*r1(t) * math.sin(t)) for t in np.arange(0.,2*math.pi,0.1)], cycle=True))

