from tdtool import *

setglops("->")
print(drawPath([(0,0,0),(3,0,0)]))
print(drawPath([(0,0,0),(0,5,0)]))
print(drawPath([(0,0,0),(0,0,3)]))

r2 = 7.1**2

def surface(x,y):
    return np.array((
            x,y,
            math.sqrt(r2-x**2-(y-1)**2) - 5
            ))


setglops("gray")
for x in np.linspace(0,3,7):
    print(drawPath([surface(x,y) for y in np.linspace(0,4,11)]))
for y in np.linspace(0,4,9):
    print(drawPath([surface(x,y) for x in np.linspace(0,3,11)]))

setglops("blue")

def gamma(t):
    return (1.5+math.cos(t) + .1*math.sin(4*t), 2+math.sin(t)+.2*math.cos(3*t))

print(drawPlot(surface(*gamma(t)) for t in np.linspace(0,2*math.pi, 20)))
