#!/usr/bin/env python3
# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson8
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson8
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson8

# git add circle_class.py
# git add test_circle.py
# git commit circle_class.py
# git commit test_circle.py

# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson8/
# click Pull request > new pull request

class Circle(object):
    pi = 3.14

    def __init__(self, usr_radius):
        self.radius = round(float(usr_radius), 2)
        self.usr_diameter = round(float(usr_radius * 2),2)

    @property # radius getter
    def radius(self):
        return self.usr_radius

    @radius.setter
    def radius(self, value):
        self.usr_radius = value

    @property  # diameter getter
    def diameter(self):
        return  self.usr_diameter

    @diameter.setter
    def diameter(self, value):
        self.usr_diameter = value
        self.radius = value / 2
        return self.usr_diameter

    @property
    def area(self):
        a = round(Circle.pi * (self.radius * self.diameter),2)
        return a

    @property
    def circumference(self):
        c = round(Circle.pi * int(self.diameter),2)
        return c

    @classmethod
    def from_diameter(cls, d):
        cls.cls_diameter = d
        radius = d / 2
        return cls(radius)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return  f"Circle({self.radius})"

    def __add__(self, other):
        return f"Circle({self.radius + other.radius})"

    def __mul__(self, n):
        return f"Circle({self.radius * n})"

    __rmul__ = __mul__

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False


print("")
print(">>Step 1:")
c = Circle(10)
print("the radius: " + str(c.radius))

print("")
print(">>Step(s) 2-3:")
c.diameter = 50
my_new_diameter = str(c.diameter)
print("the new diameter: " + str(my_new_diameter))
my_new_radius = c.radius
print("the new radius: " + str(my_new_radius))

print("")
print(">>Step 4:")
area = c.area
print("the area: " + str(area))
circumference = c.circumference
print("the new circumference: " + str(circumference))

print("")
print(">>Step 5:")
c = Circle.from_diameter(8)
print("the diameter: " + str(c.cls_diameter))
print("the radius: " + str(c.radius))
circumference = c.circumference
print("the circumference: " + str(circumference))
area = c.area
print("the area: " + str(area))

print("")
print(">>Step 6:")
c = Circle(4)
print(c)
print(repr(c))
d = eval(repr(c))
print(d)

print("")
print(">>Step 7:")
c1 = Circle(2)
c2 = Circle(4)
print(c1 + c2)
print(c2 * 3)
print(3 * c2)

print("")
print(">>Step 8:")
c1 = Circle(2)
c2 = Circle(4)
print(c1 > c2)
print(c2 > c1)
print(c2 == c1)
c3 = Circle(4)
print(c2 == c3)
circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
print(circles)
circles.sort()
print(circles)

print("")
print(">>Step 8 (opt):")
a_circle = Circle(10)
print(a_circle * 3 == 3 * a_circle) # True


