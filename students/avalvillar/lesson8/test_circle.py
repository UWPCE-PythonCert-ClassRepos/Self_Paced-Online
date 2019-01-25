"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 22th 2019
"""

'''
This is the testing class associated with the circle.py class. All below
functions passed using the pytest -vv command
'''

import circle as c

#Step 1: Create a class called Circle with required Radius
def test_radius():
    cir = c.Circle(10)
    assert cir.radius == 10, ('Step 1: Radius')

#Step 2: Add a "diameter" property
def test_diameter():
    cir = c.Circle(20)
    assert cir.diameter == 40, ('Step 2: Diameter')

#Step 3: Add a setter for "diameter" (properties)
def test_diameter_property():
    cir = c.Circle(10)
    cir.diameter = 10
    assert cir.diameter == 10, ('Step 3: Diameter Property (diameter)')
    assert cir.radius == 5, ('Step 3: Diameter Property (radius)')

#Step 4: Add an area property
def test_area_property():
    cir = c.Circle(10)
    assert cir.area == 314.159265, ('Step 4: Area Property')

#Step 5: Alternate constructor using diameter
def test_alternate_circle():
    cir = c.Circle.from_diameter(8)
    assert cir.radius == 4, ('Step 5: Alternate Circle (radius)')
    assert cir.diameter == 8, ('Step 5: Alternate Circle (diameter)')

#Step 6: Adding __str__ and __repr__ methods to the class
def test_str_repr():
    cir = c.Circle(4)
    assert str(cir) == 'Circle with radius: 4', ('Step 6: str')
    assert repr(cir) == '\'Circle(4)\'', ('Step 6: repr')
    assert eval(repr(cir)) == 'Circle(4)', ('Step 6: eval repr')

#Step 7: Adding numeric protocols for two circls
def test_numerics():
    c1 = c.Circle(2)
    c2 = c.Circle(4)
    c3 = c1 + c2
    assert eval(repr(c3)) == 'Circle(6)', ('Step 7: c1 + c2 = c3')
    c4 = c2 * 3
    assert eval(repr(c4)) == 'Circle(12)', ('Step 7: c2 * 3 = c4')
    c5 = 3 * c2
    assert eval(repr(c4)) == 'Circle(12)', ('Step 7: 3 * c2 = c5')

#Step 8: Adding compare functions
def test_compares():
    c1 = c.Circle(2)
    c2 = c.Circle(4)
    c3 = c.Circle(4)
    assert (c1 > c2) == False, ('Step 8: c1 > c2 = False')
    assert (c1 < c2) == True, ('Step 8: c1 < c2 = True')
    assert (c1 == c2) == False, ('Step 8: c1 == c2 = False')
    assert (c2 == c3) == True, ('Step 8: c2 == c3 = True')

#Sorting of Circles
def test_sorting():
    c1 = c.Circle(9)
    c2 = c.Circle(8)
    c3 = c.Circle(6)
    c4 = c.Circle(7)
    c5 = c.Circle(2)
    circles = [c1, c2, c3, c4, c5]
    before_sort = str(circles)
    assert before_sort == "['Circle(9)', 'Circle(8)', 'Circle(6)', 'Circle(7)', 'Circle(2)']", ('Unsorted Circles')
    after_sort = str(sorted(circles))
    assert after_sort == "['Circle(2)', 'Circle(6)', 'Circle(7)', 'Circle(8)', 'Circle(9)']", ('Sorted Circles')