from circle import Circle

def test_step1():
    c = Circle(5)
    assert c.radius == 5
    

def test_step2():
    c = Circle(5)
    assert c.diameter == 10