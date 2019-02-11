#!/usr/bin/env python3
"""
Create a class called Circle with various properties and methods
Author: JohnR
Version: 0.9
Last updated: 2/10/2019
Notes: base functionality in place
"""


class Circle(object):
    """
    Circle class for some basic math functions such as area, equality, etc.
    """
    pi = 3.14159

    def __init__(self, radius=5):
        self.radius = radius
        self.area = round(self.radius * self.radius * Circle.pi)

    def __repr__(self):
        return f'A circle where pi={Circle.pi} and radius={self.radius}'

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError(f'{val} is not a valid number')
        self._radius = val

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @staticmethod
    def sort_key(self):
        return self.radius

    def circumference(self):
        return round(self.radius * Circle.pi * 2)


dd = Circle()
print(dd.circumference())
