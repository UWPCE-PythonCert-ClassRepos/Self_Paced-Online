import io
import pytest

from circle_class import *

#def result(x):
#    outfile = io.StringIO()
#    x.the_radius(outfile)
#    return outfile.getvalue()



    
#Step 1 tests
def test_radius():
    c = Circle(40)
#    file_contents = result(c)
    assert c.radius == 40
#    print(file_contents)
#    assert False
    
def test_diameter():
    c = Circle(80)
#    file_contents = result(c)
    assert c.diameter == 160
