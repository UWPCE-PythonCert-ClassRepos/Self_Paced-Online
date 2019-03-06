#Class for creating and manipulating circles
import math
from functools import total_ordering

@total_ordering
class Circle:

    _diameter = 0
    pi = math.pi
    _area = 0
    circles = []

    def __init__(self, radius, diameter=None):
        self.radius = radius
        self.diameter = radius*2
        self.circles.append(self)

    def __str__ (self):
        return 'Circle with radius: ' + str(self.radius)

    def __repr__ (self):
        return 'Circle(' + str(self.radius) + ')'

    def __add__ (self, circle2):
        return Circle(self.radius + circle2.radius)

    def __mul__ (self, mult):
        return Circle(self.radius * mult)

    def __rmul__ (self, mult):
        return Circle(self.radius * mult)

    def __eq__ (self, circle2):
        return self.radius == circle2.radius

    def __lt__ (self, circle2):
        return self.radius < circle2.radius

    def sort_key(self):
        return self.radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        diameter = diameter
        return cls(radius, diameter)

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = self._diameter / 2

    @property
    def area(self):
        return self.pi * self.radius * 2

def main():
    pass


if __name__ == '__main__':
    main()