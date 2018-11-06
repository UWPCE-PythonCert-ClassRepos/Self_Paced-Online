import math

class Circle:
  def __init__(self, radius):
      self._radius = radius
      self._area = round(math.pi * radius ** 2, 6)

  @property
  def radius(self):
      return self._radius

  @property
  def diameter(self):
      return self._radius * 2

  @diameter.setter
  def diameter(self, diameter):
      self._radius = diameter/2

  @property
  def area(self):
    return self._area

  @classmethod
  def from_diameter(class_object, diameter):
      return class_object(diameter/2)

  def __str__(self):
      return "Circle with radius: %.6f"% (self._radius)

  def __repr__(self):
      return "Circle({})".format(int(self._radius))

  def __add__(self, other):
      return Circle(self._radius + other._radius)

  def __mul__(self, other):
      return Circle(self._radius * other)

  def __lt__(self, other):
      return self._radius < other._radius

  def __gt__(self, other):
      return self._radius > other._radius

  def __eq__(self, other):
      return self._radius == other._radius

  def __iadd__(self, another):
      self._radius += another._radius
      return self

  def __imul__(self, another):
      self._radius *= another._radius
      return self
