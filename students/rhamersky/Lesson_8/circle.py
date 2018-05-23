#!/usr/bin/env python3
# Description: This program will calculate circles.
# Developer: Ryan Hamersky
# Date: 05/19/2018
# Rev: New

# -----Data Section-----
import math
lst_radius = []

# -----Process Section-----
# This class creates circles by using the radius or diameter.
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, set_diameter):
        return cls(set_diameter/2)


    @property
    def diameter(self):
        return round(2*self.radius, 2)

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = round(new_diameter/2, 2)

    @property
    def area(self):
        circle_area = math.pi*self.radius**2
        return round(circle_area, 2)


    def __add__(self, another_circle):
        sum = self.radius + another_circle.radius
        return sum

    def __mul__(self, number):
        multiply = self.radius * number
        return multiply

    def __gt__(self, another_circle):
        return self.radius > another_circle.radius

    def __lt__(self, another_circle):
        return self.radius < another_circle.radius

    def __eq__(self, another_circle):
        return self.radius == another_circle.radius

    def __str__(self):
        return "Circle with radius: {:.02f}.".format(self.radius)

    def __repr__(self):
        return "Circle({:.0f})".format(self.radius)

    def sort_key(self):
        return self.radius



# -----Presentation Section-----
