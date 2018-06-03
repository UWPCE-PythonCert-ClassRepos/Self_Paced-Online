#!/usr/bin/env python3

# chmod +x circle.py needs to be performed before executable

'''
    File Name: test_html_render.py
    Author: Matt Hudgins
    Date created: 6/2/18
    Date last modified: 6/2/18
    Python Version 3.6.4
'''

from math import pi

class Circle():
    """This function creates a class for circles"""
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def raduius(self, value):
        if value < 0:
            raise ValueError('Must have a value greater than 0')
        self.radius = value

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
            if value < 0:
                raise ValueError('Must have a value greater than 0')
            self.radius = value / 2

    @property
    def area(self):
        return pi * self.raduius ** 2

    def __str__(self):
        return 'Circle({})'.format(self.radius)

    def __repr__(self):
        return'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)
