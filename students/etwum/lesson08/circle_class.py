class Circle():

    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, radius):
        self.radius = radius



c = Circle(3)

print(c.diameter)