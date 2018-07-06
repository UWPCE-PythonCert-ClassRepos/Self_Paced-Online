import math


class Circle(object):
    def __init__(self, the_radius):
        self._radius = the_radius
        self._diameter = self._radius*2
        self._area = math.pi*self._radius**2

    @classmethod
    def from_diameter(cls_object, the_diam):
        return cls_object(the_diam/2)

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diam_val):
        self._radius = diam_val/2
        self._diameter = diam_val
        self._area = math.pi*self._radius**2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, rad_val):
        self._radius = rad_val
        self._diameter = self._radius*2
        self._area = math.pi*self._radius**2

    @property
    def area(self):
        return self._area

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __str__(self):
        return "Circle with radius: {}".format(self._radius)

    def __add__(self, other):
        return Circle(self._radius + other._radius)

    def __mul__(self, value):
        return Circle(self._radius*value)

    def __truediv__(self, value):
        return Circle(self._radius/value)

    def __rmul__(self, value):
        return Circle(self._radius*value)

    def __lt__(self, other):
        return self._radius < other._radius

    def __eq__(self, other):
        return self._radius == other._radius
