import math
__author__ = "Wieslaw Pucilowski"


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be greater than zero")
        else:
            self._radius = value

    @property
    def area(self):
        return self._radius ** 2 * math.pi

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2 # setting diameter through radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius) # returns new Circle instance

    def __mul__(self, other):
        return Circle(self.radius * other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __iadd__(self, other):
        self.radius += other.radius
        return self     # returns updated instance

    def __imul__(self, other):
        self.radius *= other.radius
        return self
