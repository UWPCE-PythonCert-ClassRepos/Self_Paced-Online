import math


class Circle:
    """represents a simple circle, using properties, a class method, and
    special methods"""

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Circle with radius: ' + str(self.radius)

    def __repr__(self):
        return 'Circle(' + str(self.radius) + ')'

    def __add__(self, other):
        self.radius += other.radius
        return self.__repr__()

    def __mul__(self, value):
        self.radius *= value
        return self.__repr__()

    def __rmul__(self, value):
        return self.__mul__(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def from_diameter(self):
        return self.diameter
