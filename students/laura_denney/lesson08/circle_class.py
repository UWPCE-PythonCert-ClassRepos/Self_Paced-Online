#-------------------------------------------------#
# Title: Circle Class
# Dev:   LDenney
# Date:  December 9, 2018
# ChangeLog: (Who, When, What)
#   Laura Denney, 12/09/18, Started Circle Class Assignment
#-------------------------------------------------#

from math import pi

class Circle(object):
    _diameter = None
    _area = None

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = .5 * value
        self._area = round(pi * self.radius **2,5)

    @property
    def area(self):
        return self._area

#alternate constructor to create circle by diameter
    @classmethod
    def from_diameter(Circle, diameter):
        self = Circle(diameter/ 2)
        return self

    def __init__(self,radius):
        self.radius = radius
        self.diameter = radius * 2
        self._area = round(pi * radius **2, 5)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        if type(other) is Circle:
            return Circle(self.radius + other.radius)
        else:
            return Circle(self.radius + other)

    def __radd__(self, other):
        return Circle(self.radius + other)

    def __mul__(self, other):
        if type(other) is Circle:
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __truediv__(self, other):
        if type(other) is Circle:
            return Circle(self.radius / other.radius)
        else:
            return Circle(self.radius / other)

    def __idiv__(self, other):
        return self / other


    def __iadd__(self, other):
        return self + other

    def __imul__(self, other):
        return self * other


