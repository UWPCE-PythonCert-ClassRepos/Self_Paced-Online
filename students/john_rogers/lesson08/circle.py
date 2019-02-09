#!/usr/bin/env python3
"""
Create a class called Circle with various properties and methods
Author: JohnR
Version: 0.4
Last updated: 2/09/2019
Notes: base functionality in place
"""


class Circle:
    """
    Circle class for some basic math functions such as area.
    Make pi static and create a default for radius.
    3) add two circles together
    4) compare two circles for equality
    5)  be able to put them in a list and sort them
    """
    pi = 3.14159

    def __init__(self, radius=1):
        self.radius = radius
        self.area = self.radius * self.radius * Circle.pi

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    def __repr__(self):
        return f'A circle where pi={Circle.pi} and radius={self.radius}'

    def get_circumference(self):
        return self.radius * Circle.pi * 2

