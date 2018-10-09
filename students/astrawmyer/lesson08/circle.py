class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = 2*radius
        
    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self.radius = diameter/2

c = Circle(5)
print(c.radius)
print(c.diameter)