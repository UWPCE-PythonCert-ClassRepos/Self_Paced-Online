'''
file: circle.py
elmar_m / 22e88@mailbox.org
Lesson08: circle class
'''

import math as m

class Circle:

    def __init__(self, r):
        if isinstance(r, (int, float, complex)) and r > 0:
            self._radius = r
            self._diameter = r * 2
        else:
            # raise TypeError('Only numerical datatypes greater than zero allowed')
            raise BaseException('Only numerical datatypes greater than zero allowed')

    @property
    def radius(self):
        # print('getter radius called')
        return self._radius

    @radius.setter
    def radius(self, new_r):
        # print('setter radius called with ', new_r)
        self._radius = new_r 
        self._diameter = 2 * self._radius

    @property
    def diameter(self):
        # print('getter diameter called')
        return self._diameter
    
    @diameter.setter
    def diameter(self, new_dia):
        # print('setter diameter called with ', new_dia)
        self._diameter = new_dia
        self._radius = self._diameter / 2


    @property 
    def area(self):
        # print('getter area called')
        self._area = (self._radius ** 2) * m.pi
        return self._area

    
    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)


    def __str__(self):
        return 'Circle with radius: {}'.format(self._radius)
    
    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __add__(self, second):  
        return Circle(self._radius + second.radius)

    def __mul__(self, factor):
        return Circle(self._radius * factor)
    
    def __rmul__(self, factor):
        return Circle(self._radius * factor)

    def __lt__(self, second):
        return self._radius < second.radius

    def __gt__(self, second):
        return self._radius > second.radius

    def __eq__(self, second):
        return self._radius == second.radius
    
    def sortkey(self):
        return self._radius


