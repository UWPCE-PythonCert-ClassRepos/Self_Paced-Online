import math

class Circle:

	def __init__(self, radius):
		self._radius = radius


	@property
	def radius(self):
		"""return radiuis """
		return self._radius
	
	@property
	def diameter(self):
		return self._radius * 2

	@diameter.setter
	def diameter(self, value):
		self._radius = value /2

	@property
	def area(self):
		return math.pi * self._radius**2
	
	def __repr__(self):
		return "Circle({})".format(self._radius)

	def __str__(self):
		return "Circle with radius: {}".format(self._radius)

	def __add__(self, other):
		if isinstance( other, Circle):
			return self._radius + other._radius
		elif isinstance(other, int ) :
			return self._radius + other

	def __mul__(self, other):
		if isinstance( other, Circle):
			return self._radius * other._radius
		elif isinstance(other, int ) :
			return self._radius * other
		

	def __lt__(self, other):
		return self._radius < other._radius

	def __le__(self, other):
		return self._radius <= other._radius

	def __eq__(self, other):
		return self._radius == other._radius

	def __ge__(self, other):
		return self._radius >= other._radius

	def __gt__(self, other):
		return self._radius > other._radius

	def __ne__(self, other):
		return self._radius != other._radius



class Sphere(Circle):
	def __repr__(self):
		return "Sphere({})".format(self._radius)

	def __str__(self):
		return "Sphere with radius: {}".format(self._radius)

	@property
	def volume(self):
		return (4/3) * math.pi * self._radius**3

	@property
	def area(self):
		if isinstance(self, Sphere):
			return 4 * math.pi * self._radius**2
		else:
			raise NotImplementedError
	




