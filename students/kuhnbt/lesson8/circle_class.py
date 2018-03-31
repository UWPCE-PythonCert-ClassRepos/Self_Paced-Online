from math import pi
from functools import total_ordering


@total_ordering
class Circle:
    """A class representing a circle"""
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self._radius = radius
        self._diameter = self.radius * 2
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value
        self._diameter = value * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError('Diameter must be positive')
        self._diameter = value
        self._radius = value / 2

    @property
    def area(self):
        return self._radius**2 * pi

    @classmethod
    def from_diameter(cls, diameter):
        if diameter <= 0:
            raise ValueError('Diameter must be positive')
        self = cls(diameter / 2)
        self._diameter = diameter
        return self

    def __str__(self):
        return 'A Circle with radius {:.2f}'.format(self._radius)

    def __repr__(self):
        return 'Circle ({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, num):
        return Circle(self.radius * num)

    def __truediv__(self, num):
        return Circle(self.radius / num)

    def __rmul__(self, num):
        return self.__mul__(num)

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __idiv__(self, other):
        return self.__div__(other)

    def __pow__(self, other):
        return Circle(self.radius**other)
