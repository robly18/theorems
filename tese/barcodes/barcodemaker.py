from itertools import chain
import math


glops = {}

def renderOption(key,value):
    if key != "options":
        return "{}={}".format(key,value)
    else:
        return value

def renderPoint(p):
    return "({:.3f},{:.3f})".format(*p)
    
def getOptionsString(optsdict):
    return ",".join(
                chain((renderOption(key,glops[key]) for key in glops if key not in optsdict),
                      (renderOption(key,optsdict[key]) for key in optsdict)))
                      
def drawCustom(pathspec, **opts):
    return "\\draw[{}] {};".format(getOptionsString(opts), pathspec)
    

def drawLine(*path, **opts):
    return drawCustom("--".join(renderPoint(p) for p in path), **opts)
def drawNode(pos, name, **opts):
    return "\\node[{}] at {} {{{}}};".format(getOptionsString(opts), renderPoint(pos), name)


class Barcode:
    tags = []

    rows = []
    currentrow = None
    
    margin = 2
    minx, maxx = 0,0
    
    #parameters for drawing
    tickHeight = 0.2
    
    startY = -0.5
    spaceBetweenBars = -0.4
    spaceBetweenRows = -0.6
    
    barcodeLabelMargin = 1
    
    def _updateBounds(self, pos):
        if pos==math.inf:
            return
        self.minx = min(pos,self.minx)
        self.maxx = max(pos,self.maxx)

    def addTag(self, pos, name):
        self.tags.append((pos,name))
        self._updateBounds(pos)
        return self

    def addBar(self, start, end, label):
        self.currentrow.append((start,end,label))
        self._updateBounds(start)
        self._updateBounds(end)
        return self

    def addRow(self, name):
        self.currentrow = []
        self.rows.append((name,self.currentrow))
        return self
        
    def printBar(self, start, end, label, y):
        if end != math.inf:
            pass
        elif end == math.inf:
            return drawCustom("{}--{} node[right] {{{}}}".format(renderPoint((start,y)),renderPoint((self.maxx+self.margin*0.85,y)), label), options="(-,thick")

    def printBarcode(self): #add option to print vertically?
        yield drawLine((self.minx-self.margin,0),(self.maxx+self.margin,0),options="->,thick")
        for (x,name) in self.tags:
            yield drawCustom("{}--{} node[above] {{{}}}".format(renderPoint((x,-self.tickHeight)),renderPoint((x,self.tickHeight)), name))
        
        currentY = self.startY
        
        for (name, row) in self.rows:
            labelY = currentY
            for bar in row:
                yield self.printBar(*bar, currentY)
                currentY += self.spaceBetweenBars
            currentY -= self.spaceBetweenBars
            labelY = (labelY + currentY)/2
            yield drawNode((self.maxx+self.margin+self.barcodeLabelMargin, labelY), name)
            currentY += self.spaceBetweenRows

a = 2.5 / 2

bcphi = Barcode().addTag(0,"0").addTag(2*a,"$2a$").addTag(-2*a,"$-2a$")
bcphi.addRow("$(\CF_{-1})$").addBar(-2*a,math.inf,"$B_0$")
bcphi.addRow("$(\CF_0)$").addBar(0,math.inf,"$B_1$").addBar(0,math.inf,"$B_2$")
bcphi.addRow("$(\CF_1)$").addBar(2*a,math.inf,"$B_3$")

print("\n".join(bcphi.printBarcode()))

