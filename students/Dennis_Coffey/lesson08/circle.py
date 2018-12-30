# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 22:04:31 2018

@author: dennis
"""
import math


""" The Circle Class """

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({:.0f})'.format(self.radius)
    
    # Adds two circles together by adding radius for each 
    # and creating new circle with new radius
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # Creates new circle by multiplying original circle radius by defined value
    def __mul__(self, other):
        self.radius *= other

    # Creates new circle by multiplying original circle radius by defined value
    # when inputs are reversed
    def __rmul__(self, other):
        self.radius *= other

    def __lt__(self, other):
        return self.radius < other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return round(self._radius**2 * math.pi, 6)

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2
        
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

# Step 1 output
c = Circle(4)
print(c.radius)

# Step 2 output
print(c.diameter)

# Step 3 output
c.diameter = 4
print(c.radius)
print(c.diameter)

# Step 4
print(c.area)

# Step 5
c = Circle.from_diameter(8)
print(c.diameter)
print(c.radius)

# Step 6
print(c)
print(repr(c))
print(eval(repr(c)))
print(eval(repr(c)).radius)

# Step 7
c1 = Circle(2)
c2 = Circle(4)
c3 = Circle(2)
c3 = c1 + c2
print(c3)
c2 * 3
print(c2.radius)
3 * c1
print(c1.radius)

# Step 8
print('Comparison')
print(c1 < c2)
print(c2 < c1)
print(c1 > c2)
print(c2 > c1)
print(c1 <= c2)
print(c2 >= c1)
print(c1 >= c3)
print(c1 <= c3)
print(c1 == c3)
print(c1 == c2)

circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
print(circles)
circles.sort()
print(circles)
