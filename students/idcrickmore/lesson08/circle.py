""" script to describe circles"""

import math

class Circle:
    
    # step 1
    def __init__(self, radius):
        self.radius = radius
        
    # step 2
    @property
    def diameter(self):
        return self.radius*2
        
    # step 3
    @diameter.setter
    def diameter(self, val):
        self.radius = val/2
    
    # step 4
    @property
    def area(self):
        return math.pow(self.radius, 2) * math.pi
        
    # step 5
    @classmethod
    def from_diameter(cls, val):
        return cls(val/2)

    # step 6
    def __str__(self):  
        return "Circle with a radius of {}." .format(self.radius)