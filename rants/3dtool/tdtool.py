import numpy.matlib as np
import math

sq2 = math.sqrt(2)

def projMatrix(alpha, h):
    ch = math.sqrt(1 - h**2)
    return np.mat(
        [[math.cos(alpha), math.sin(alpha), 0],
         [-math.sin(alpha)*ch, math.cos(alpha)*ch, h]])

def setPM(alpha, h):
    global pm
    pm = projMatrix(alpha,h)
setPM(math.pi*.6, .9)

def showPair(mat):
    return "({:.3f},{:.3f})".format(mat[0,0],mat[0,1])

def go3dto2d(pt):
    return pm.dot(pt)

def showPt(pt):
    if type(pt) is str:
        return pt
    return showPair(go3dto2d(pt))

glops = ""
def setglops(arg):
    global glops
    glops = arg
def drawPath(points, options=None):
    if options is None:
        options = glops
    return "\\draw[{}] {}; ".format(options,"--".join(map(showPt, points)))
def drawPoint(pt, options=None):
    if options is None:
        options = glops
    return "\\node[{}] at {} {{}}; ".format(options,showPt(pt))

def drawPlot(points, options=None):
    if options is None:
        options = glops
    return "\\draw[{}] plot[smooth] coordinates{{{}}}; ".format(options," ".join(map(showPt, points)))