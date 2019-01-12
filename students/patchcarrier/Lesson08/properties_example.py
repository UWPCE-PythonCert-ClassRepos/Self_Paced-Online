#!/usr/bin/env python

"""
Example code for properties

NOTE: if your getters and setters are this simple: don't do this!

"""


class C:
    def __init__(self):
        self._x = 100
    @property
    def x(self):
        #print("in getter")
        return self._x
    @x.setter
    def x(self, value):
        #print("in setter", value)
        if value > 100:
            self._x = 100
        elif value < 0:
            self._x = 0
        else:
            self._x = value
    @x.deleter
    def x(self):
        del self._x

if __name__ == "__main__":
    c = C()
    c.x = 5
    print(c.x)
    c._x = 87
    print(c.x)

