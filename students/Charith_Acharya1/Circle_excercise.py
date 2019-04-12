# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:05:17 2019

@author: acharch
"""


import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.__area = radius ** 2 * math.pi

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def circle_area(self):
         self.area = math.pi * self.radius * self.radius
         return self.area 
     
    @classmethod
    def circle_from_diameter(cls, diameter):
        cls.area_dia = math.pi * diameter/2 * cls.diameter/2
        return cls.area_dia
    
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __iadd__(self, another):
        self.radius += another.radius
        return self

    def __imul__(self, another):
        self.radius *= another.radius
        return self

    
        

    
    
        