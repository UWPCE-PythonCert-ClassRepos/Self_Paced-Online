# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:39:49 2018

@author: Karl M. Snyder
"""
import math

from functools import total_ordering

@total_ordering
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @classmethod #alternate constructor to instantiate Circle with Dia.
    def from_diameter(cls, value):
        return cls(value/2)
  
    @property #this is needed before @diameter.setter
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = self._diameter/2
        
    @property
    def area(self):
        return round(math.pi * self.radius**2, 2)
    
    def __str__(self):
        return "Circle with radius: {:.2f}".format(self.radius)
    
    def __repr__(self):
        return "Circle({})".format(self.radius)
    
    def __add__(self, other):
        return self.radius + other.radius
    
    def __mul__(self, other):
        if isinstance(other, Circle):
            return self.radius * other.radius
        else:
            return self.radius * other
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    
    