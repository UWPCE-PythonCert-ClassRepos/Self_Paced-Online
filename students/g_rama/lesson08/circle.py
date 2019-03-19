import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self,diameter):
        self.radius = int(diameter/2)

    @property
    def area(self):
        return math.pi * (self.radius * 2)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(int(diameter/2))

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return f'Circle({self.radius + other.radius})'

    def __mul__(self, other):
        return f'Circle({self.radius*other})'

    def __rmul__(self, other):
        return f'Circle({self.radius*other})'

    def __le__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius




    #
    # @property
    # def diameter(self):
    #     return self._radius * 2
    #
    # @diameter.setter
    # def diameter(self, diameter):
    #     self._diameter = radius *2
    #     return self.diameter


if __name__ == '__main__':
    c = Circle(3)
    print(c.radius)
    print(c.diameter)
    c.diameter = 4
    print(c.diameter)
    print(c.radius)
    print(c.area)
    c = Circle.from_diameter(8)
    print(c.diameter)
    print(c.radius)
    c = Circle(4)
    print(c)
    print(repr(c))
    d = eval(repr(c))
    print(d)
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1+c2)
    print(c2*3)
    print(3*c2)
    print(c1<c2)
    print(c1>c2)
    print(c1==c2)
    c3 = Circle(4)
    print(c2 == c3)
    circles=[Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    print(circles)
    circles.sort()
    print(circles)






