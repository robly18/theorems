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
    def __init__(self):
        self.tags = []

        self.rows = []
        self.currentrow = None
        
        self.margin = 2
        self.minx, self.maxx = 0,0
        
        #parameters for drawing
        self.tickHeight = 0.2
        
        self.startY = -0.5
        self.spaceBetweenBars = -0.4
        self.spaceBetweenRows = -0.6
        
        self.barcodeLabelMargin = 1
    
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
        tip="(-"
        if end == math.inf:
            end = self.maxx+self.margin*0.85
        else:
            tip="{(-]}"
        return drawCustom("{}--{} node[right] {{{}}}".format(renderPoint((start,y)),renderPoint((end,y)), label), options=tip+",thick")

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
            if name!="":
                yield drawNode((self.maxx+self.margin+self.barcodeLabelMargin, labelY), name)
            currentY += self.spaceBetweenRows

a = 3.1415

def findroot(f, lo, hi, eps): #assumes f(lo) < 0 < f(hi)
    mid = (lo + hi)/2
    if -eps < f(mid) < eps:
        return mid
    elif f(mid) < 0:
        return findroot(f,mid,hi,eps)
    else:
        return findroot(f,lo,mid,eps)

x0 = findroot(lambda x: a*0.5*math.sin(x) - x, math.pi/2, 0, 0.00001)
beta = a * math.cos(x0)

midnode = 4*x0**2 + 4*beta - 1

bcphi = Barcode().addTag(0,"0").addTag(2*a,"$2a$").addTag(-2*a,"$-2a$")
bcphi.addRow("$(\CF_{-1})$").addBar(-2*a,math.inf,"$B_0$")
bcphi.addRow("$(\CF_0)$").addBar(0,math.inf,"$B_1$").addBar(0,math.inf,"$B_2$")
bcphi.addRow("$(\CF_1)$").addBar(2*a,math.inf,"$B_3$")

#print("\n".join(bcphi.printBarcode()))

bcphi2 = Barcode().addTag(0,"0").addTag(-4*a,"$-4a$").addTag(4*a,"$4a$").addTag(-midnode,"$-4 x_0^2 - 4 \\beta$").addTag(midnode,"$4 x_0^2 + 4 \\beta$")
bcphi2.addRow("$(\CF_{-2})$").addBar(-4*a,math.inf,"$B_0$")
bcphi2.addRow("$(\CF_{-1})$").addBar(-midnode,math.inf,"$A_0$").addBar(-midnode,math.inf,"$A_1$")
bcphi2.addRow("$(\CF_0)$").addBar(0,math.inf,"$B_1$").addBar(0,math.inf,"$B_2$")
bcphi2.addRow("$(\CF_{1})$").addBar(midnode,math.inf,"$C_0$").addBar(midnode,math.inf,"$C_1$")
bcphi2.addRow("$(\CF_{2})$").addBar(4*a,math.inf,"$B_3$")

bcphi2.spaceBetweenRows = -1.35
bcphi2.spaceBetweenBars = -1.2
bcphi2.margin = 1.2
bcphi2.barcodeLabelMargin = 3
bcphi2.startY = -1.2

#print("\n".join(bcphi2.printBarcode()))

bcphi2h = Barcode().addTag(0,"0").addTag(-4*a,"$-4a$").addTag(4*a,"$4a$").addTag(-midnode,"$-4 x_0^2 - 4 \\beta$").addTag(midnode,"$4 x_0^2 + 4 \\beta$")
bcphi2h.addRow("$(\HF_{-2})$").addBar(-4*a,-midnode,"")
bcphi2h.addRow("$(\HF_{-1})$").addBar(-midnode,math.inf,"")
bcphi2h.addRow("$(\HF_0)$").addBar(0,math.inf,"").addBar(0,math.inf,"")
bcphi2h.addRow("$(\HF_{1})$").addBar(midnode,math.inf,"").addBar(midnode,4*a,"")

bcphi2h.spaceBetweenRows = -1.5
bcphi2h.spaceBetweenBars = -1.2
bcphi2h.margin = 1.5
bcphi2h.barcodeLabelMargin = 3
bcphi2h.startY = -1.2

#print("\n".join(bcphi2h.printBarcode()))

a = 0.8

bcphi20 = Barcode().addTag(0,"0").addTag(-4*a,"$-4a$").addTag(4*a,"$4a$")
bcphi20.addRow("$(\CF_{-1})$").addBar(-4*a,math.inf,"$B_0$")
bcphi20.addRow("$(\CF_0)$").addBar(0,math.inf,"$B_1$").addBar(0,math.inf,"$B_2$")
bcphi20.addRow("$(\CF_{1})$").addBar(4*a,math.inf,"$B_3$")


#print("\n".join(bcphi20.printBarcode()))

bct1 = Barcode().addTag(0,"$z_1$").addTag(1,"$z_2$").addTag(2,"$z_3$").addTag(3,"$z_4$")
bct1.addRow("").addBar(1,math.inf,"").addBar(2,math.inf,"")

bct1.spaceBetweenBars = -0.3
bct1.margin = 0.3

#print("\n".join(bct1.printBarcode()))

bcex = Barcode().addTag(0,"$0$").addTag(1,"$1$").addTag(2,"$2$")
bcex.addRow("").addBar(0,1,"").addBar(1,math.inf,"").addBar(2,math.inf,"")

print("\n".join(bcex.printBarcode()))
