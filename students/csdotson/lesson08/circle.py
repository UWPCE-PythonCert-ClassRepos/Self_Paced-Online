#!/usr/bin/env python3
import math

class Circle:
    """Create a Circle class representing a simple circle"""

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return ( cls(diameter/2) )
        
    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return (math.pi * math.pow(self.radius, 2))

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2
