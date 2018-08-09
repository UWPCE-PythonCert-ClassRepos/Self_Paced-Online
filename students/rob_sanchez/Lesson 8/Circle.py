#!/usr/bin/env python3


class Circle:

    # Circle class init class
    # Returns the radius of a circle
    def __init__(self, radius):
        self.radius = radius

    # Returns teh diameter of a circle
    @property
    def diameter(self):
        return self.radius * 2
