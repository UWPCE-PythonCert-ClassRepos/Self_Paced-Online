# lesson 8 assignment to make a circle class
import math

class Circle:

    def __init__(self, radius):
        self.radius=radius

    @property
    def diameter(self):
        return 2*self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2


    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        text = "Circle with radius {:.6f}".format(self.radius)
        return text


    def __repr__(self):
        text = "Circle({})".format(self.radius)
        return text


    def __add__(circle1, circle2):
        circlesum = Circle((circle1.radius + circle2.radius))
        return circlesum


    def __mul__(val1, val2):
        if type(val1) == "int":
            circleprod = Circle((val2.radius * val1))
        else:
            circleprod = Circle((val1.radius * val2))
        return circleprod


    def __lt__(circle1, circle2):
        if circle1.radius < circle2.radius:
            return True
        else:
            return False


    def __le__(circle1, circle2):
        if circle1.radius <= circle2.radius:
            return True
        else:
            return False


    def __eq__(circle1, circle2):
        if circle1.radius == circle2.radius:
            return True
        else:
            return False


    def __ge__(circle1, circle2):
        if circle1.radius >= circle2.radius:
            return True
        else:
            return False


    def __gt__(circle1, circle2):
        if circle1.radius > circle2.radius:
            return True
        else:
            return False


    def __ne__(circle1, circle2):
        if circle1.radius != circle2.radius:
            return True
        else:
            return False