#!/usr/bin/env python3
import math

class Circle:
    """Create a Circle class representing a simple circle"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return (math.pi * math.pow(self.radius, 2))

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2



    # def test_diameter_changes_radius(self):
    #     circle = Circle(4)
    #     circle.diameter = 4
    #     assert circle.radius == 2:
    #         print("success!!")
