from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, dval):
        self.radius = dval / 2

    @property
    def area(self):
        return 2*pi*self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __add__(self,other):
        return Circle(self.radius + other.radius)

    def __mul__(self,num):
        return Circle(self.radius * num)

    def __lt__(self,other):
        return self.radius < other.radius

    def __gt__(self,other):
        return self.radius > other.radius

    def __eq__(self,other):
        return self.radius == other.radius

    def __iadd__(self, other):
        self.radius = self.radius + other.radius
        return self
