import math


class Circle(object):
    def __init__(self, radius):
        if radius >=0 :
            self.radius = radius
        else:
            raise TypeError("Invalid radius passed")

    @classmethod
    def from_diameter(class_object, diameter):
        if diameter >= 0:
            return class_object(diameter / 2)
        else:
            raise TypeError("Invalid diameter passed")

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * math.pow(self.radius, 2)

    @radius.setter
    def radius(self, value):
        self._radius = value

    @diameter.setter
    def diameter(self, value):
        self.radius = (value / 2)

    def __str__(self):
        return f'Circle with radius {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, new):
        return Circle(self.radius + new.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius 

    def __ge__(self, other):
        return self.radius >= other.radius 


# c = Circle(4)
# c.diameter = 2
# print (c.diameter)
# print (c.radius)


# c = Circle(2)
# print (c.area)
# c.area = 42 #error

# c = Circle.from_diameter(8)
# print (c.radius)

# print (c.diameter)

# print (c)
# d = eval(repr (c))
# print(d)

c1 = Circle(2)
c2 = Circle(4)
c3 = Circle(4)

print(c1+c2)
print(c2 * 3)
print(3 * c2)

print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
print(c2 == c3)


circle_list = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
print(circle_list)
circle_list.sort()
print(circle_list)
