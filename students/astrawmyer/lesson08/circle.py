import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

        
    @property
    def diameter(self):
        return 2 * self.radius


    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2


    @property
    def area(self):
        return (self.radius**2) * math.pi
    

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
    

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)
    

    def __repr__(self):
        return "Circle({})".format(self.radius)


    def __add__(self, other):
        new_circle = self.radius + other.radius
        return Circle(new_circle)
    

    def __mul__(self, other):
        new_circle = self.radius * other
        return Circle(new_circle)
    

    def __rmul__(self, other):
        new_circle = self.radius * other
        return Circle(new_circle)


c = Circle(5)

c1 = Circle(2)
c2 = Circle(4)
c3 = c1+c2
print(c3)