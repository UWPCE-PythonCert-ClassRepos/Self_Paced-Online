from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius * self.radius * pi

    @classmethod
    def from_diameter(cls, val):
        return cls(val / 2)

    def __repr__(self):
        return(f"Circle {self.radius}")

    def __str__(self):
        return(f"Circle with radius: {self.radius}")

    def __add__(self, circle_2):
        return self.radius + circle_2.radius

    def __mul__(self, value):
        return self.radius * value

    def __eq__(self, circle):
        return self.radius == circle_2.radius

    def __lt__(self, circle_2):
        return self.radius < circle_2.radius

    def __gt__(self, circle_2):
        return self.radius > circle_2.radius

    def __le__(self, circle_2):
        return self.radius <= circle_2.radius

    def __ge__(self, circle_2):
        return self.radius >= circle_2.radius

    def __ne__(self, circle_2):
        return self.radius != circle_2.radius
