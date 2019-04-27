from pylab import *
import numpy as np



'''
(y-hy)**2 + (x-hx)**2 = r**2
y**2 - 2*hy*y + hy**2 + x**2 - 2*x*hx + hx**2 - r**2 = 0
y1 = hy + sqrt(hy**2 - (hy**2 + x**2 - 2*x*hx + hx**2 - r**2))
y1 = hy + sqrt(-x**2 + 2*x*hx - hx**2 + r**2)
y2 = hy - sqrt(- 2 * x**2 + 4*x*hx - 2 * hx**2 + 2 * r**2)
>>> h = (1,1)
>>> r = 0.5
>>> draw_circle(h, r)






m = (y - py) / (x - px)
y - py = m*x - m*px
y = m*x + py - m*px

'''
def draw_circle(h, r, accuracy=100):
	hx, hy = h
	r2 = r**2
	xlim = (hx - r, hx + r)
	xdiap = xlim[1] - xlim[0]
	xstep = xdiap / accuracy
	x = linspace(xlim[0], xlim[1], accuracy, True)
	
	y1 = hy + np.sqrt(
		-x**2 + 2*x*hx - hx**2 + r**2
	)	
	y2 = hy - np.sqrt(
		-x**2 + 2*x*hx - hx**2 + r**2
	)
	plot(x, y1)
	plot(x, y2)
	
	
	axis('equal')

def draw_line(p1, p2, margins=10):
	if p1[0] > p2[0]:
		p1, p2 = p2, p1
	x1, y1 = p1
	x2, y2 = p2

	if x1 == x2:
		pass
	else:
		m = (y2 - y1) / (x2 - x1)
		b = y1 - m*x1
		x = np.linspace(x1-margins, x2+margins, 2, True)
		y = x*m + b
		plot(x, y)
		
	
def draw_line2(p1, m, margin=10):
		x1, y1 = p1
		b = y1 - m*x1
		x = np.linspace(x1-margins, x2+margins, 2, True)
		y = x*m + b
		plot(x, y)

def get_m(p1,)

h2 = (1,1)
h1 = (1-np.sqrt(0.75),1.5)	
intersect = ((h2[0] + h1[0])/2, (h2[1] + h1[1])/2)
draw_circle(h1, 0.5)
draw_circle(h2,0.5)	
draw_line(h1, h2, 0.5)
plot(intersect[0], intersect[1], 'ro')
show()
