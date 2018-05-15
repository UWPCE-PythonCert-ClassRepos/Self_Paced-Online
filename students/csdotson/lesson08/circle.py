#!/usr/bin/env python3
import math

class Circle:
    """Create a Circle class representing a simple circle"""

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("radius can't be less than 0")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("radius can't be less than 0")
        self._radius = val

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @classmethod
    def from_diameter(cls, diameter):
        return ( cls(diameter/2) )

    @property
    def area(self):
        return (math.pi * math.pow(self.radius, 2))

    def __lt__(self, other):
        """ Define less than comparator for circles """
        return (self.radius < other.radius)

    def __eq__(self, other):
        return(self.radius == other.radius)

    def __add__(self, other):
        """ Add radii of two circles """
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError("Both objects need to be circles")

    def __sub__(self, other):
        """ Subtract radii of two circles """
        if isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        else:
            raise TypeError("Both objects need to be circles!")

    def __mul__(self, val):
        """ Multiply self by val: Circle * 4 """
        return Circle(self.radius * val)

    def __rmul__(self, val):
        """ Multiply val by self: 4 * Circle """
        return Circle(self.radius * val)

    def __truediv__(self, val):
        """ Divide self by val: Circle / 4 """
        return Circle(self.radius / val)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)
