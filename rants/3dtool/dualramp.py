from tdtool import *

import numpy

setPM(math.pi*.15,.9)
setglops("->")
print(drawPath([(0,0,0),(6,0,0)]))
print(drawPath([(0,0,0),(0,4,0)]))
print(drawPath([(0,0,0),(0,0,2)]))


setglops("gray")
for x in np.arange(1,6.1):
    print(drawPath([(x,0,0),(x,4,0)]))
for y in np.arange(1,4.1):
    print(drawPath([(0,y,0),(6,y,0)]))

a = numpy.matrix((2,1))
b = numpy.matrix((5,3))

d = b-a

perp = .2*numpy.matrix((-d[0,1],d[0,0]))

def surface(v):
    return (v[0,0],v[0,1],.1*numpy.inner(b, b-v)[0,0])
def ground(v):
    return (v[0,0],v[0,1],0)

vertices = [start+perp*sign for (start,sign) in ((a,1),(b,1),(b,-1),(a,-1))];


setglops("blue!20,thick")
for t in numpy.linspace(0,1,13,endpoint=False)[1:]:
    print(drawPath([surface(a+perp+t*d),surface(a-perp+t*d)]))

setglops("blue,thick")
print(drawPath(map(surface,vertices), cycle=True))

setglops("red,thick")
print(drawPath((ground(a),surface(a))))
print(drawPoint(ground(b)))
