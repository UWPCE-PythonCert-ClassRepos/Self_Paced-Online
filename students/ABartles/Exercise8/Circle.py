import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, dia):
        self.radius = dia / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, dia):
        return cls(dia / 2)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Circle(self.radius * other)
        elif type(other) == Circle:
            return Circle(self.radius * other.radius)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    # >
    def __gt__(self, other):
        return self.radius > other.radius

    # <
    def __lt__(self, other):
        return self.radius < other.radius

    # ==
    def __eq__(self, other):
        return self.radius == other.radius
