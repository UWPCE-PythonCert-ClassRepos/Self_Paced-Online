import pytest
from io import StringIO
import html_render as h

def test_element():
    test_element = h.Element()
    test_element.append("This is content.")
    test_element.append("This is more content.")
    assert test_element.content[0] == "This is content."
    assert test_element.content[1] == "This is more content."

def test_render():
    f = StringIO()
    test_render = h.Element()
    test_render.append("This is content.")
    test_render.render(f)
    page = f.getvalue()
    expected_page = '<html>\n    This is content.\n</html>\n'
    assert page == expected_page

def test_html_element():
    f = StringIO()
    test_html = h.Html()
    test_html.render(f)
    page = f.getvalue()
    expected_page = '<!DOCTYPE html>\n<html>\n</html>\n'
    assert page == expected_page

def test_body_element():
    f = StringIO()
    test_body = h.Body()
    test_body.render(f)
    page = f.getvalue()
    expected_page = '<body>\n</body>\n'
    assert page == expected_page

def test_p_element():
    f = StringIO()
    test_p = h.P()
    test_p.render(f)
    page = f.getvalue()
    expected_page = '<p>\n</p>\n'
    assert page == expected_page

def test_head_element():
    f = StringIO()
    test_head = h.Head()
    test_head.render(f)
    page = f.getvalue()
    expected_page = '<head>\n</head>\n'
    assert page == expected_page

def test_onelinetag_element():
    f = StringIO()