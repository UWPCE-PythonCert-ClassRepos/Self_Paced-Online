import math

class Circle():
    def __init__(self, the_radius=None):
        self.radius = the_radius

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return self.radius*self.radius*math.pi

    @classmethod
    def from_diameter(circle, diameter):
        self = circle()
        self.diameter = diameter
        return self
