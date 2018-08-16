#!/usr/bin/env python3

from math import pi
from functools import total_ordering

@total_ordering
class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        self._radius = radius
        self._diameter = radius * 2

    @classmethod
    def from_diameter(cls, diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be greater than 0.")
        self = cls(diameter / 2)
        return self

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be greater than 0.")
        self._diameter = diameter
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        self._diameter = radius * 2
        self._radius = radius

    @property
    def area(self):
        return (self._radius ** 2) * pi

    def sort_key(self):
        return self._radius

    def __str__(self):
        return "Circle with radius {:.2f}".format(self._radius)

    def __repr__(self):
        return "Circle({})".format(self._radius)

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius - other._radius)
        else:
            return Circle(self._radius - other)

    def __rsub__(self, other):
        if isinstance(other, Circle):
            return Circle(other._radius - self._radius)
        else:
            return Circle(other - self._radius)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other._radius)
        else:
            return Circle(self._radius + other)

    def __radd__(self, other):
        if isinstance(other, Circle):
            return Circle(other._radius + self._radius)
        else:
            return Circle(other + self._radius)

    def __truediv__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius / other._radius)
        else:
            return Circle(self._radius / other)

    def __rtruediv__(self, other):
        if isinstance(other, Circle):
            return Circle(other._radius / self._radius)
        else:
            return Circle(other / self._radius)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        else:
            return Circle(self._radius * other)

    def __rmul__(self, other):
        if isinstance(other, Circle):
            return Circle(other._radius * self._radius)
        else:
            return Circle(other * self._radius)

    def __lt__(self, other):
        return self._radius < other._radius

    def __eq__(self, other):
        return self._radius == other._radius

    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other._radius
        else:
            self._radius += other
        return self

    def __isub__(self, other):
        if isinstance(other, Circle):
            self.radius -= other._radius
        else:
            self._radius -= other
        return self

    def __imul__(self, other):
        if isinstance(other, Circle):
            self.radius *= other._radius
        else:
            self._radius *= other
        return self

    def __itruediv__(self,other):
        if isinstance(other, Circle):
            self.radius /= other._radius
        else:
            self._radius /= other
        return self

if __name__ == '__main__':
    c = Circle(4)
    print(c)
    print(repr(c))



