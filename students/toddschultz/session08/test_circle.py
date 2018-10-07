from circle import Circle

def test_radius():
	a = Circle(4)
	assert a.radius is 4

def test_diameter_1():
	b = Circle(4)
	assert b.diameter is 8

def test_diameter_2():
	c = Circle(4)
	c.diameter = 10
	assert c.diameter is 10

def test_from_diameter():
	d = Circle.from_diameter(8)
	assert d.radius is 4.0