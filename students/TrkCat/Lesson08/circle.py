from math import pi
from functools import total_ordering


@total_ordering
class Circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('radius cannot be negative')
        self._radius = val

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, val):
        return cls(val / 2)

    def __str__(self):
        return ('Circle with radius: {}'.format(self.radius))

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        if (self.radius - other.radius < 0):
            raise ValueError('produces circle of negative radius')
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __truediv__(self, other):
        return Circle(self.radius / other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def sort_key(self):
        return self.radius
