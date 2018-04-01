import math

class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            self._radius = 0
        else:
            self._radius = radius

    @property
    def diameter(self):
        return self._radius*2

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            self._radius = 0
        else:
            self._radius = diameter / 2

    @property
    def area(self):
        return math.pow(self._radius,2) * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self

    def __str__(self):
        return f"Circle with radius: {self._radius}"

    def __repr__(self):
        return f"Circle({self._radius})" 

    def __add__(self, other_circle):
        self._radius += other_circle.radius
        return self

    def __mul__(self, factor):
        self._radius *= factor
        return self

    __rmul__ = __mul__

    def __lt__(self, other_circle):
        return True if self._radius < other_circle.radius else False        

    def __eq__(self, other_circle):
        return True if self._radius == other_circle.radius else False 
