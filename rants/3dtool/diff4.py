from tdtool import *
setPM(math.pi*.7,.9)

setglops("->")
print(drawPath([(0,0,0),(3,0,0)]))
print(drawPath([(0,0,0),(0,4,0)]))
print(drawPath([(0,0,0),(0,0,3)]))

r2 = 7.1**2

def surface(x,y):
    return np.array((
            x,y,
            math.sqrt(r2-x**2-(y-1)**2) - 5
            ))


setglops("gray")
for x in np.linspace(0,3,7):
    print(drawPlot([surface(x,y) for y in np.linspace(0,4,11)]))
for y in np.linspace(0,4,9):
    print(drawPlot([surface(x,y) for x in np.linspace(0,3,11)]))

setglops("->,blue")

for x in np.arange(.5,3.5,1):
    for y in np.arange(.5,4.5,1):
        print(drawPath([(x,y,0),(x,y,3)]))
        print(drawPoint(surface(x,y),"atom"))