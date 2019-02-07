#!/usr/bin/env python3
"""
Create a class called Circle with various properties and methods
Author: JohnR
Version: 0.1
Last updated: 2/07/2019
Notes: first pass, creating a generic circle class without using
        any magic methods/ decorators/ etc.
"""


class Circle:
    """
    circle class for some basic math functions such as area
    Note: Define instance by either radius or diameter
    1) compute area
    2) print circle and get something nice
    3) add two circles together
    4) compare two circles for equality
    5)  be able to put them in a list and sort them
        A) use properties
        B) classmethod
        C) self-defined special methods
    """
    pi = 3.14159

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def __repr__(self):
        pass

    def get_circumference(self):
        return self.radius * Circle.pi * 2



