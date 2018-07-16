import math


class Circle:

    # step 1
    def __init__(self, radius):
        self.radius = radius

    # step 2
    @property
    def diameter(self):
        return self.radius*2

    # step 3
    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    # step 4
    @property
    def area(self):
        return math.pow(self.radius, 2) * math.pi

    # step 5
    @classmethod
    def from_diameter(cls, val):
        return cls(val/2)

    # step 6.1
    def __str__(self):
        return "Circle with a radius of {}." .format(self.radius)

    # step 6.2
    def __repr__(self):
        return "Circle({})" .format(self.radius)

    # step 7.1
    def __add__(self, circle2):
        return Circle(self.radius + circle2.radius)

    # step 7.2
    def __mul__(self, num):
        return Circle(self.radius * num)

    # step 8.1
    def __gt__(self, other):
        return (self.radius > other.radius)

    # step 8.2
    def __lt__(self, other):
        return (self.radius < other.radius)

    # step 8.3
    def __eq__(self, other):
        return (self.radius == other.radius)

    # step 8.4
    def __ne__(self, other):
        return (self.radius != other.radius)
