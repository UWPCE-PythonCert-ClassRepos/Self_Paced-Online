


class Circle():
    """A circle object that has all the attributes and methods of a circle"""
    _radius = None

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius_in):
        if radius_in > 0:
            self._radius = radius_in
        else:
            raise(ValueError('The radius must be a positive number'))


    @property
    def diameter(self):
        return 2*self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __repr__(self):
        return f'Circle({self.radius})'
