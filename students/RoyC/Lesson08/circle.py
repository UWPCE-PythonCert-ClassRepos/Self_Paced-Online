#!/usr/bin/env python3

from math import pi

class Circle:
    """
    Class for a circle object
    """
    def __init__(self, radius):
        self._radius = radius
        
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