import math
import itertools

def digits(t, b): #assumes t < b
	mantissa = b
	while True:
		mantissa /= b
		digit = math.floor(t/mantissa)
		t -= digit * mantissa
		yield digit

template = "\draw[thick, {3}, {{[-)}}] ({0:.2f}, {2}) -- ({1:.2f}, {2});"


def pt(ints, y, color="blue"):
    for (a, b) in ints:
        print(template.format(a*10,b*10,y, color))

def intervals(t, b, depth):
    digs = list(itertools.islice(digits(t,b), depth))
    digs[-1] += 1
    x = 0
    for i, d in enumerate(digs):
        for k in range(d):
            yield ((x, x+b**(-i)), i)
            x += b**(-i)

t = 0.83
b = 3
A = [(0,1/3),(1/3,1/3+1/9),(1/3+1/9,1/3+2/9),(1/3+2/9,2/3),(2/3,2/3+1/9),(2/3+2/9,2/3+2/9+1/27)]

pt(A, -.4)

#pt([(0,1/3),(1/3,2/3),(2/3,2/3+1/9),(2/3+1/9,2/3+1/9+1/27)], -6, "gray")

