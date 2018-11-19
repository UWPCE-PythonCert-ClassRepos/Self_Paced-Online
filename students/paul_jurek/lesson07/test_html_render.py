"""test suite for html render exercise"""

import html_render as hr

def test_Element_run_error_free():
    """tests Element call runs without error"""
    hr.Element()
    assert 1 == 1

def test_Element_append():
    """tests an element can run append method
    testing this runs without error"""
    page = hr.Element()
    page.append('this is something more')
    assert 1 == 1

def test_Element_render():
    """tests element has render function"""
    page = hr.Element()
    page.render(file_out='test_file.html')
    assert 1 == 1
