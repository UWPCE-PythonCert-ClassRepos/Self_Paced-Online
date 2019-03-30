from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self._diameter = radius*2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value/2

    @property
    def area(self):
        return pi*self.radius**2

    @classmethod
    def from_diameter(cls, value):
        self = cls(value/2)
        return self

    def __str__(self):
        return "Circle with radius: {0:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({0:.0f})". format(self.radius)

    def __add__(self, other):
        return Circle(self.radius+other.radius)

    def __mul__(self, other):
        return Circle(self.radius*other)

    def __rmul__(self, other):
        return Circle(self.radius*other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __truediv__(self, other):
        return Circle(self.radius / other)

    def __iadd__(self, other):
        return Circle(self.radius + other.radius)

