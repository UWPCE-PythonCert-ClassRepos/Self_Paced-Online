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

 

