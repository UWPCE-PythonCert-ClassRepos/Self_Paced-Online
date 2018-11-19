"""test suite for html render exercise"""

import pytest

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

def test_Element_start_tag():
    """tests start tag formatted correct"""
    page = hr.Element()
    assert page._start_tag == '<>'

def test_Element_end_tag():
    """tests start tag formatted correct"""
    page = hr.Element()
    assert page._end_tag == '</>'

def test_html_element_has_html_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.Html()
    assert element.tag == 'html'

def test_body_element_has_body_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.Body()
    assert element.tag == 'body'

def test_p_element_has_p_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.P()
    assert element.tag == 'p'