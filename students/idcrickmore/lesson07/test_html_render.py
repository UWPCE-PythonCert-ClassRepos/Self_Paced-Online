"""tests the html_render.py file"""

from html_render import element

def test_content():
    input = (element('this is a test'))
    assert input.content == ['this is a test']