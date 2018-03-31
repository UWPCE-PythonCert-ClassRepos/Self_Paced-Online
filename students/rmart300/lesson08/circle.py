class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            self._radius = 0
        else:
            self._radius = radius
