from math import pi

class Circle:

    def __init__(self, the_radius):
        self.radius = the_radius
        self._diameter = 2 * the_radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, myval):
        self._diameter = myval
        self.radius = myval/2

    @property
    def area(self):
        area = pi * (self.radius) ** 2
        return area

    @classmethod
    def from_diameter(cls, myval):
        self = cls(myval)
        self._diameter = myval
        self.radius = myval/2
        return self

    def __str__(self):
        return 'Circle with a radius: {}'.format(self.radius)

    def __repr__(self):
        return "'Circle({})'".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def sort_key(self):
        return self.radius
