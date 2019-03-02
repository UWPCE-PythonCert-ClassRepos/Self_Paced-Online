# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:33:15 2019
@author: Florentin Popescu
"""

#===================LESSON_08====================

#================================================
# Part 1: Circle class
#================================================

# imports
from math import pi
#------------------------------------------------

class Circle:
    
    def geometry(self, _geometry):
        if not _geometry:
            raise NameError("Input geometry must be defined and not null.")            
        elif isinstance(_geometry, str):
            raise NameError("Input geometry must be numeric.")
        elif _geometry < 0:
            raise ValueError("Input geometry must be positive.")
            
    #--------------------------------------------    
    # Step 1
    """
    Initializer for numeric data member 'radius' 
    """
    def __init__(self, radius):
        if not Circle.geometry(self, radius):
            self.radius = radius

    #--------------------------------------------    
    # Step 2
    """
    Return diameter as twice the value of data member 'radius' 
    """
    @property
    def diameter(self):
        return self.radius * 2
        
    #--------------------------------------------    
    # Step 3
    """
    Set the diameter and change it via re-setting the data mamber 'radius' 
    """
    @diameter.setter
    def diameter(self, diameter):
        if not Circle.geometry(self, diameter):
            self.radius = diameter / 2

    #--------------------------------------------    
    # Step 4
    """
    Return area via formula: 'area = pi * radius^{2}' 
    """
    @property
    def area(self):
        return pi * pow(self.radius, 2)
      
    #--------------------------------------------    
    #Step 5
    """
    Create the circle from diameter
    """
    @classmethod
    def from_diameter(cls, diameter):
        if not Circle.geometry(cls, diameter):
            return cls(diameter / 2)

    #--------------------------------------------    
    # Step 6
    """
    Define .__str__() and .__repr__() methods for the Circle class
    """
    def __str__(self):
        return f"Circle's radius = {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"

    #--------------------------------------------    
    # Step 7 
    """
    Two circles addition (commutative algebraic operation; 'c1+c2 == c2+c1')
    """
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(sum([self.radius, other.radius]))
        else:
            raise AttributeError("Both additions must be circles")
    
    """
    Circle's expansion via its radius multiplication 
    """
    def __mul__(self, multiplier):
        if isinstance(multiplier, (int, float)) and multiplier > 0:
            return Circle(self.radius * multiplier)
        else:
            raise ValueError("Multiplier must be numeric and positive")
    
    def __rmul__(self, multiplier):
        if isinstance(multiplier, (int, float)) and multiplier > 0:
            return Circle.__mul__(self, multiplier)
        else:
            raise ValueError("Multiplier must be numeric and positive")
    
    #--------------------------------------------    
    # Step 8
    """
    Compare two circles  
    """
    #less then (<)
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise AttributeError("Both additions must be circles")
   
    #greater then (>) --> logical equivalent !(<) 
    def __gt__(self, other):
        return not Circle.__lt__(self, other)
        
    #equality
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise AttributeError("Both additions must be circles")

    #--------------------------------------------    
    # Step 9
    """
    Augumented assignment operator
    """
    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
        else:
            raise AttributeError("Both additions must be circles")
        return self

#================================================
#--------------- END ----------------------------
#================================================

