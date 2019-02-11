#!/usr/bin/env python3
"""
Create a class called Circle with various properties and methods
Author: JohnR
Version: 0.9
Last updated: 2/11/2019
Notes: TODO: able to set area currently - should throw an attribute error
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

    def __str__(self):
        return f'A circle where pi={Circle.pi} and radius={self.radius}'

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError(f'{val} is not a valid number.')
        self._radius = val

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        if val < 0:
            raise ValueError(f'{val} is not a valid number.')
        self.radius = val / 2

    @staticmethod
    def sort_key(self):
        return self.radius

    def circumference(self):
        return round(self.radius * Circle.pi * 2)

