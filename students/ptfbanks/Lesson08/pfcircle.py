#!/usr/bin/env python3

#---------------------------
# Lesson 8  Circle Build - add-compare - list 
#---------------------Set-up----------------------------------#)

#-------Import / Librarys-----------------------------------#
import io
import math

#-----class Circle/ Attributes / properties------------
class Circle:

    def __init__(self, radius):
        self.radius = radius
        
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property    
    def circum(self):
        return math.pi * self.diameter 

#-----Step 6 STR / repr-------------

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return'Circle of radius: {}'.format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

#-----Step 7 Numeric protocol------------

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        multi = self.radius * other
        return Circle(multi)

    def __rmul__(self, other):
        multi = self.radius * other
        return Circle(multi)

 #-----Step8  Comparisons------------   
 
    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius
