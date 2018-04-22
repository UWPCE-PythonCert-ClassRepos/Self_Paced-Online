#!/usr/bin/python


class Circle(object):

    def __init__(self, the_radius):
        self._radius = the_radius

    def get_radius(self):
        return self._radius

    def set_radius(self, the_radius):
        if type(the_radius) in ['str', 'list', 'tuple', 'dict']:
            raise TypeError("Radius entry must be a positive, non-string value")
        else:
            if the_radius < 0:
                raise ValueError("Radius must be greater than 0")
            else:
                self._radius = the_radius

    radius = property(get_radius, set_radius)

