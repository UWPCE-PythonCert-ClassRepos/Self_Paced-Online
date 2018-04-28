#!/usr/bin/python


class Circle(object):

    @staticmethod
    def entry_check(the__radius):
        if isinstance(the__radius, (str, list, tuple, dict)):
            raise TypeError("Radius entry must be a single, positive, and "
                            "non-string value")
        else:
            if the__radius < 0:
                raise ValueError("Radius must be greater than 0")
            else:
                return the__radius

    def __init__(self, the_radius):
        self._radius = self.entry_check(the_radius)

    def get_radius(self):
        return self._radius

    def set_radius(self, the_radius):
        self._radius = self.entry_check(the_radius)

    radius = property(get_radius, set_radius)

