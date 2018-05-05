import math


class Circle:
    """represents a simple circle, using properties, a class method, and
    special methods"""

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Circle with radius: ' + str(self.radius)

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
