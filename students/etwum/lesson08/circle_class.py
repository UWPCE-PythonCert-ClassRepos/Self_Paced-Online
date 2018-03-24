from math import pi


class Circle():

    def __init__(self,radius):
        self.radius = radius
        self.__area = pi * radius**2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, radius):
        self.radius = radius/2

    @property
    def area(self):
        return self.__area

    @classmethod
    def get_diameter(cls,diameter):
        return cls(diameter/2)


c = Circle.get_diameter(6)

print(c.diameter)
print(c.radius)