from math import pi

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self.radius * 2
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2

    @property
    def area(self):
        return self._radius**2 * pi

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter / 2)
        self._diameter = diameter
        return self

    def __str__(self):
        return 'A Circle with radius {:.2f}'.format(self._radius)

    def __repr__(self):
        return 'Circle ({})'.format(self.radius)
    
    def __add__(self, other):
        return(Circle(self.radius + other.radius))