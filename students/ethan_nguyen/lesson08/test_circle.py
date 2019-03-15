"""
test code for circle.py

"""

import io
import pytest
from circle import *


########
# Step 1
########

def test_circle():
    """
    Test circle
    """
    c1 = Circle(4)
    c2 = Circle(5)
    c3 = Circle(9)

    list_circle = [c3, c1, c2]

    list_circle.sort()

    assert list_circle[0] == c1

    # making sure the content got in there.
    assert c1.radius == 4
    assert c1.diameter == 8
    assert "Circle" in str(c1)
    assert "Circle" in repr(c1)
    assert c1.area == round(math.pi * c1.radius * c1.radius, 4)
    assert Circle(3) - Circle(3) == Circle(0)
    assert c1 + c2 == Circle(9)
    assert Circle(5) - Circle(4) == Circle(1)
    assert Circle(2) * 3 == Circle(6)
    assert 3 * Circle(2)  == Circle(6)
    c1 += Circle(1)
    assert c1 == Circle(10)
    c1 *= 2
    assert c1 == Circle(20)
    assert Circle(3) < Circle(4)
    assert Circle(5) > Circle(3)

    
def test_sphere():
    """
    Test circle
    """
    s1 = Sphere(4)
    s2 = Sphere(5)

    # making sure the content got in there.
    assert s1.radius == 4
    assert s1.diameter == 8
    assert "Sphere" in str(s1)
    assert "Sphere" in repr(s1)
    assert s1.area == round(4 * math.pi * s1.radius * s1.radius, 4)
    assert s1.volume == round((s1.area * s1.radius)/3, 4)
    assert Circle(3) - Sphere(3) == Sphere(0)
    assert s1 + s2 == Sphere(9)
    assert Sphere(5) - Sphere(4) == Sphere(1)
    assert Sphere(2) * 3 == Sphere(6)
    assert 3 * Sphere(2)  == Sphere(6)
    s1 += Sphere(1)
    assert s1 == Sphere(10)
    s1 *= 2
    assert s1 == Sphere(20)
    assert Sphere(3) < Sphere(4)
    assert Sphere(5) > Sphere(3)