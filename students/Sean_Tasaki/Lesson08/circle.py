from math import pi
"""
Sean Tasaki
6/24/2018
Lesson08.circle
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return self._radius * self._radius * pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self._radius)
    
    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __add__(self, other):
        return Circle(self._radius + other._radius)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


    
  