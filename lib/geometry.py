class Vertex:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	
class Edge:
	def __init__(self, origin, target):
		self.origin = origin
		self.target = target
		xdif = self.target.x - self.origin.x
		self.m = None
		if xdif != 0:
			self.m = (self.target.y - self.origin.y) / xdif
			self.b = self.target.y - self.m * self.target.x
	
	def y(self, x):
		if self.m is None:
			return None
		return self.m * x + self.b
		
	def draw(self, margins=0):
		if x1 == x2:
			pass
		else:
			m = (y2 - y1) / (x2 - x1)
			b = y1 - m*x1
			x = np.linspace(x1-margins, x2+margins, 2, True)
			y = x*m + b
			plot(x, y)
		
	def __sub__(self, rhs):
		x = None
		if self.m == rhs.m:
			if self.m is None and self.origin.x != rhs.origin.x or self.b != rhs.b:
				return []
			else:

				return [self.origin, self.target, rhs.origin, rhs.target]
			
			
		elif self.m is None or rhs.m is None:
			x = self.origin.x if self.m is None else rhs.origin.x
		else:
			m = self.m - rhs.m

			if m != 0:
				b = self.b - rhs.b
				x = -b / m
				
		if x is not None:
			y = self.y(x)
			return [Vertex(x, y)]
		return []
			
	def __str__(self):
		return (
			'Edge('
			'origin: {origin.x}, {origin.y}, '
			'target: {target.x}, {target.y})'
		).format(**vars(self))
