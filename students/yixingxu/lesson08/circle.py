from math import pi

class Circle():
    def __init__(self, the_radius):
        self.radius = the_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, the_diameter):
        self.radius = the_diameter / 2

    @property
    def area(self):
        return 2*pi*self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, multiple):
        return Circle(self.radius * multiple)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius