#!/usr/bin/env python3

from math import pi

class Circle:
    """
    Class for a circle object
    """
    def __init__(self, radius):
        if (radius > 0):
            self._radius = radius
        else:
            raise ValueError("Radius must be a postive number")
        
    @classmethod
    def from_diameter(cls, diameter):
        """ Create new Circle with given diameter """
        self = cls(diameter / 2)
        return self
        
    @property
    def radius(self):
        return self._radius
        
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        
    @property
    def diameter(self):
        return self._radius * 2
        
    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter/2
        
    @property
    def area(self):
        return pi * self.radius**2
        
    def __str__(self):
        return "Circle with radius {:.4f}".format(self._radius)
        
    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __add__(self, other):
        """ addition operator """
        if isinstance(other, Circle):
            return Circle(self._radius + other._radius)
        else:
            return Circle(self._radius + other)
            
    def __radd__(self, other):
        """ reflected addition operator """
        if isinstance(other, Circle):
            return Circle(other._radius + self._radius)
        else:
            return Circle(other + self._radius)
            
    def __sub__(self, other):
        """ subtraction operator """
        if isinstance(other, Circle):
            return Circle(self._radius - other._radius)
        else:
            return Circle(self._radius - other)
            
    def __rsub__(self, other):
        """ reflected subtraction operator """
        if isinstance(other, Circle):
            return Circle(other._radius - self._radius)
        else:
            return Circle(other - self._radius)
            
    def __mul__(self, other):
        if isinstance(other, Circle):
            """ multiplication operator """
            return Circle(self._radius * other._radius)
        else:
            return Circle(self._radius * other)
            
    def __rmul__(self, other):
        """ reflected multiplication operator """
        if isinstance(other, Circle):
            return Circle(other._radius * self._radius)
        else:
            return Circle(other * self._radius)
            
    def __truediv__(self, other):
        """ division operator """
        if isinstance(other, Circle):
            return Circle(self._radius / other._radius)
        else:
            return Circle(self._radius / other)
            
    def __rtruediv__(self, other):
        """ reflected division operator """
        if isinstance(other, Circle):
            return Circle(other._radius / self._radius)
        else:
            return Circle(other / self._radius)
            
    def __lt__(self, other):
        return self._radius < other._radius

    def __eq__(self, other):
        return self._radius == other._radius

if __name__ == '__main__':
    c = Circle(4)
    print(c)
    print(repr(c))
        