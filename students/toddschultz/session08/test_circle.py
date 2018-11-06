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

def test_add():
	e = Circle(4)
	f = Circle(6)
	assert e.radius + f.radius is 10
	assert e.diameter + f.diameter is 20

def test_mul():
	g = Circle(4)
	h = Circle(6)
	assert g.radius * h.radius is 24
	assert g.diameter * h.diameter is 96

def test_rmul():
	i = Circle(4)
	assert 3 * i.radius is 12
	assert 3 * i.diameter is 24

def test_eq():
	j = Circle(4)
	k = Circle(4)
	assert j == k

def test_lt():
	l = Circle(4)
	m = Circle(8)
	assert l < m

def test_gt():
	n = Circle(8)
	o = Circle(4)
	assert n > o

def test_le():
	p = Circle(4)
	q = Circle(4)
	assert p <= q

def test_ge():
	r = Circle(8)
	s = Circle(8)
	assert r >= s

def test_ne():
	t = Circle(8)
	u = Circle(4)
	assert t != u

def test_sub():
	v = Circle(2)
	w = Circle(4)
	assert w - v is 2





















