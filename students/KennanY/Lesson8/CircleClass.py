import math

class Circle:

    '''Compute the circle’s area
    Print the circle and get something nice
    Be able to add two circles together
    Be able to compare two circles to see which is bigger
    Be able to compare to see if there are equal
    (follows from above) be able to put them in a list and sort them'''

    def __init__(self, radius):
        self._radius=radius
        self._diameter=radius*2

    @property
    def area(self):
        return math.pi * (self._radius**2)

    # Print circle
    def __str__(self):
        return "Circle with radius {}".format(str(self._radius))

    #Add two circles
    def __add__(self, other):
        sum= self._radius + other._radius
        return Circle(sum)

    #Circle comparisons
    def __lt__(self, other):
        return self._radius < other._radius

    def __gt__(self, other):
        return self._radius > other._radius

    def __eq__(self, other):
        return self._radius == other._radius

    #Sort
    def sort_circle(self):
        return self.radius

    #Diameter property
    @classmethod
    def diameter(self):
        return self._radius * 2

    #Alternate constructor
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)