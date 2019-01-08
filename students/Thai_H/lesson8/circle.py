

from math import pi
from math import pow


class Circle:

    #Step 1:
    ########
    def __init__(self, the_radius):
        self.radius = the_radius


    # Step 2:
    #########
    @property
    def diameter(self):
        return self.radius * 2

    # Step 3:
    ##########
    @property
    def radius(self):
        return self._radius



    @radius.setter
    def radius(self, value):
        self._radius = value

    @diameter.setter
    def diameter(self, value):
        self.radius = (value / 2)


    # Step 4:
    ##########  area of circle
    @property
    def area(self):
        return pi * pow(self._radius , 2)  # pi * r square


    # Step 5:
    ##########  alternate way to create circle
    @classmethod
    def circle_from_diameter(class_object, diameter):
        return class_object(diameter / 2)


    # Step 6:
    ##########
    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    # Step 7:
    #########
    def __add__(self, another_circle):  # add 2 circles
        return Circle(self.radius + another_circle.radius)


    def __mul__(self, another_circle):
        return Circle(self.radius * another_circle)
    def __rmul__(self, another_circle):
        return Circle(self.radius * another_circle)

    # Step 8:
    #########
    def __eq__(self, another_circle):
        return self.radius == other_circle.radius  # true if equal

    def __lt__(self, another_circle):
        return self.radius < another_circle.radius

    def __gt__(self, another_circle):
        return self.radius > another_circle.radius

# Test step 1
#c = Circle(4)
#print(c.radius)  #expected 4 got 4

# Test step 2
#c = Circle(4)
#print (c.diameter) #expected 8 got 8

# Test step 3
#c = Circle(4)  # radius = 4
#print(c.diameter) # expected 8 got 8
#c.diameter = 2 # now change diameter to 2
#print(c.radius) # radius 2/2 = 1

# Test step #4
#c = Circle(2)  # radius = 2
#print (c.area) # pi r square = 12.566370614359172


#Test step 5
#c = Circle.circle_from_diameter(8)
#print(c.diameter)  #expected 8 got 8
#print(c.radius) #expect 4 got 4


#Test step 6
#c = Circle(4)  #    "Circle with radius: 4"
#print(c)
#print(repr(c))  #   "Circle(4)"


# Test step 7
#circle_1 =  Circle(2)
#circle_2 = Circle(4)
#circle_3 = Circle(4)
#print('circle 1 + circle 2 = ', circle_1 + circle_2) #  Circle with radius: 6.0
#print('circle 1 * circle 2 = ', circle_1 * circle_2) #  Circle with radius: 8.0
#print('circle 2 * 3 = ', circle_2 * 3)  #  Circle with radius: 12
#print('3 * circle 2 = ', 3 * circle_2)  #  Circle with radius: 12

# Test step 8
#print('circle_1 > circle_2 ? ', circle_1 > circle_2) #false
#print('circle_1 < circle_2 ? ', circle_1 < circle_2) #true
#print('circle_1 == circle_2 ? ', circle_1 == circle_2) #false
#print('circle_2 == circle_3 ? ', circle_2 == circle_3) #true

#list_of_circles = [ Circle(1), Circle(8), Circle(7), Circle(6),
#                    Circle(0), Circle(3), Circle(4), Circle(3), Circle(2), Circle(9)]
#print(list_of_circles)
#list_of_circles.sort()
#print(list_of_circles)