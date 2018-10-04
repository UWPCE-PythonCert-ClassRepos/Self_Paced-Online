# Description: Circle Properties
# Author: Andy Kwok
# Last Updated: 08/29/2018
# ChangeLog: Initialization

import math

class Circle:
    
    def __init__(self, radius = None):
        self.radius = radius
        self.diameter = radius*2
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    def __str__(self):
        return "Circle with radius: {}".format(str(self.radius))
        
    def __repr__(self): 
        return "Circle({})".format(str(self.radius))
        
    def __add__(self, other):
        sum = self.radius + other.radius
        return Circle(sum)
    
    def __mul__(self, other):
        multi = self.radius * other
        return Circle(multi)
    
    def __rmul__(self, other):
        multi = self.radius * other
        return Circle(multi)
    
    #Defining comparsion properties of the class    
    def __lt__(self, other):
        #Can be change to output a different behavior/response
        return self.radius < other.radius
        
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
        
    def sort_key(self):
        return self.radius
    
