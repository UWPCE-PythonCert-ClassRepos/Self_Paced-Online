from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return pi * self.radius * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __imul__(self, other):
        self.radius *= other.radius
        return self
