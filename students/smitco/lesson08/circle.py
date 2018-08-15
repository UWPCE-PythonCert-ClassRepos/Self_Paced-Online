# lesson 08 circle class
# !/usr/bin/env python3


from math import pi

class Circle(object):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        else:
            self._radius = radius

    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, val):
        if val <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = val
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2
    
    @property
    def area(self):
        return pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    def __repr__(self):
        return "Circle({:.1f})".format(self.radius)
    
    def __str__(self):
        return "Circle: r = {:.1f}, d = {:.1f}, a = {:.1f}".format(self.radius, self.diameter, self.area)
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
        
    def __sub__(self, other):
        return Circle(self.radius - other.radius)
    
    def __mul__(self, other):
        return Circle(self.radius * other)
    
    def __rmul__(self, other):
        return Circle(self.radius * other)
    
    def __truediv__(self, other):
        return Circle(self.radius / other)
        
    def __lt__(self, other):
        return (self.radius < other.radius)
    
    def __eq__(self, other):
        return (self.radius == other.radius)