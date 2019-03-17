#!/usr/bin/env python3

import math

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return str(f"Circle with radius: {self.radius}")

    def __repr__(self):
        return repr(f'Circle({self.radius})')
        #return(self)

    def __iadd__(self, other):
        self.radius += other.radius
        return self  

    def __isub__(self, other):
        self.radius += other.radius
        return self  

    def __add__(self, other):
        self.radius = self.radius + other.radius
        return self

    def __sub__(self, other):
        self.radius = self.radius - other.radius
        return self
    
    def __mul__(self, other):
        self.radius = self.radius * other
        return self

    def __imul__(self, other):
        #####
        self.radius *=  other
        return self

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __rmul__(self, other):
        if other == 0:
            return self
        else:
            return self.__mul__(other)

    def __eq__(self, other):
        return (self.area == other.area)
    
    def __lt__(self, other):
        return (self.area < other.area)

    def __gt__(self, other):
        return (self.area > other.area)

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = self._diameter/2

    @property
    def area(self):
        return round(math.pi * (self.radius * self.radius), 4)

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(int(diameter/2))
        self.diameter = int(diameter)
        return self


class Sphere(Circle):
    def __str__(self):
        return str(f"Sphere with radius: {self.radius}")

    def __repr__(self):
        return repr(f'Sphere({self.radius})')

    @property
    def volume(self):
        return round((self.area * self.radius)/3, 4)

    @property
    def area(self):
        return round(4 * math.pi * (self.radius * self.radius), 4)

