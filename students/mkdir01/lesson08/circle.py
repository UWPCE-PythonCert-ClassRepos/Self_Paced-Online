#!/usr/bin/python

from math import pi


class Circle():

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diam):
        self._radius = diam / 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, diam):
        return cls(diam / 2)

    def __str__(self):
        return(f'Circle with radius: {self.radius:f}')

    def __repr__(self):
        return(f'Circle({self.radius})')

    def __add__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius + outer.radius)
        else:
            return Circle(self.radius + outer)

    def __radd__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius + outer.radius)
        else:
            return Circle(self.radius + outer)

    def __iadd__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius + outer.radius)
        else:
            return Circle(self.radius + outer)

    def __mul__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius * outer.radius)
        else:
            return Circle(self.radius * outer)

    def __rmul__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius * outer.radius)
        else:
            return Circle(self.radius * outer)

    def __imul__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius * outer.radius)
        else:
            return Circle(self.radius * outer)

    def __sub__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius - outer.radius)
        else:
            return Circle(self.radius - outer)

    def __rsub__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius - outer.radius)
        else:
            return Circle(self.radius - outer)

    def __isub__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius - outer.radius)
        else:
            return Circle(self.radius - outer)

    def __truediv__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius / outer.radius)
        else:
            return Circle(self.radius / outer)

    def __rtruediv__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius / outer.radius)
        else:
            return Circle(self.radius / outer)

    def __idiv__(self, outer):
        if type(outer) == Circle:
            return Circle(self.radius / outer.radius)
        else:
            return Circle(self.radius / outer)

    def __gt__(self, outer):
        if type(outer) == Circle:
            if self._radius > outer._radius:
                return True
            else:
                return False
        else:
            if self._radius > outer:
                return True
            else:
                return False

    def __lt__(self, outer):
        if type(outer) == Circle:
            if self._radius < outer._radius:
                return True
            else:
                return False
        else:
            if self._radius < outer:
                return True
            else:
                return False

    def __eq__(self, outer):
        if type(outer) == Circle:
            if self._radius == outer._radius:
                return True
            else:
                return False
        else:
            if self._radius == outer:
                return True
            else:
                return False