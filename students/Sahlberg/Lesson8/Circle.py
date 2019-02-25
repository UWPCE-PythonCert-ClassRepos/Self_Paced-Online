


class Circle(object):
    import math as m

    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
         return self.radius*2

    @property
    def area(self):
        return float(f'{Circle.m.pi * self.radius**2:.4f}')

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)

    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'Circle({self.radius:.0f})'

    def __add__(self,circle_x):
        new_circle = Circle(self.radius + circle_x.radius)
        return new_circle


c = Circle(10)
print(c)

print(repr(c))
print(c.radius)
print(c.diameter)
print(c.area)