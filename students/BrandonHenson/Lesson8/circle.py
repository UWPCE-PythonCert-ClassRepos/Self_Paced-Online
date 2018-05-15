# Brandon Henson
# 5\11\18
# Lesson 8
# Circles

import math

circles = []


class Circle(object):
    def __init__(self, the_radius):
        self.radius = the_radius
        circles.append("Circle({})".format(self.radius))

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, value):
        self.radius = int(value/2)

    @property
    def area(self):
        return self.radius*self.radius*math.pi

    @classmethod
    def circle_from_diameter(cls, value):
        return cls(int(value/2))

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with Radius: {}".format(self.radius)

    def __add__(self, circle2):
        return "Circle({})".format(self.radius + circle2.radius)

    def __mul__(self, other):
        return "Circle({})".format(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

c = Circle(10)
print(c.area)
