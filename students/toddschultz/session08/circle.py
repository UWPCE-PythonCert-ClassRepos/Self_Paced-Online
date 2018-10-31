from math import pi

class Circle:

    ''' Making Circles with codes. '''
    def __init__(self, radius):
        self.radius = radius 
        self._diameter = radius * 2
        self._area = pi * radius**2


    @property
    def diameter(self):
        return self._diameter

    @diameter.setter 
    def diameter(self, diameter):
        if diameter < 1:
            raise ValueError
        else:
            self._diameter = diameter
            self.radius = diameter / 2

    @property
    def area(self):
        return self._area

    @classmethod
    def from_diameter(cls, diameter):
        if diameter <= 0:
            raise ValueError
        self = cls(diameter / 2)
        self = self
        self.diameter = diameter
        return self

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return Circle(self.radius + other)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        return Circle(self.radius * other)

    def __rmul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius
