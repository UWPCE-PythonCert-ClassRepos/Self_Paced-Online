import sys
import copy
import math
import pathlib
from functools import total_ordering

circles = []

@total_ordering
class Circle(object):

    def __init__(self, value):
        self._radius = value
        self._diameter = self._radius * 2
        self._area = (math.pi) * (self._radius ** 2)
    
    @classmethod
    def from_diameter(self, value):
        return Circle(value/2)
        
    @property
    def radius(self):
        return self._radius
        
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = (math.pi) * (self._radius ** 2)
    @property
    def diameter(self):
        return self._radius * 2.0
        
    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2.0
        self._area = (math.pi) * (self._radius ** 2)
        
    @property
    def area(self):
        return self._area
        
#Removing this block of code will raise AttributeError if someone tries to set the area. Leaving it here for future reference.        
#    @area.setter
#    def area(self, value):
#        raise AttributeError
        
    @area.deleter
    def area(self):
        del self._area
        
    @diameter.deleter
    def diameter(self):
        del self._diameter
        
    @radius.deleter
    def radius(self):
        del self._radius
        
    def __add__(self, other_circle):
        return Circle( self._radius + other_circle._radius)
        
    def __mul__(self, other_circle):
        return Circle(other_circle * self._radius)
                        
    def __ne__(self, other_circle):
        global circles
        circles += [Circle(self._radius)]
        circles += [Circle(other_circle._radius)]
        return self._radius != other_circle._radius
        
    def __le__(self, other_circle):
        global circles
        circles += [Circle(self._radius)]
        circles += [Circle(other_circle._radius)]
        return self._radius <= other_circle._radius
        
    def __ge__(self, other_circle):
        global circles
        circles += [Circle(self._radius)]
        circles += [Circle(other_circle._radius)]
        return self._radius >= other_circle._radius
        
    def __lt__(self, other_circle):
        global circles
        circles += [Circle(self._radius)]
        circles += [Circle(other_circle._radius)]
        return self._radius < other_circle._radius
        
    def __gt__(self, other_circle):
        global circles
        circles += [Circle(self._radius)]
        circles += [Circle(other_circle._radius)]
        return self._radius > other_circle._radius
        
    def __eq__(self, other_circle):
        global circles
        circles += [Circle(self._radius)]
        circles += [Circle(other_circle._radius)]
        return self._radius == other_circle._radius
    
    def __str__(self):        
        return f'Circle with radius: {self.radius}'
        
    def __repr__(self):
        return f'Circle({self.radius})'
        
    __rmul__ = __mul__
        
        
if __name__ == '__main__':
    c = Circle(50)
