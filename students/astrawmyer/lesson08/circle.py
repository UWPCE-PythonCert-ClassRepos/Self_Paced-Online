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
    
"""     @classmethod
    def from_diameter(cls, diameter): """


c = Circle(5)
print(c.radius)
print(c.diameter)