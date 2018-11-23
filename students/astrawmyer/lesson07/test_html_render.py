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
    test_one = h.OneLineTag()
    test_one.render(f)
    page = f.getvalue()
    expected_page = '<html></html>\n'
    assert page == expected_page

#add tags with attributes

def test_title_element():
    f = StringIO()
    test_title = h.Title()
    test_title.render(f)
    page = f.getvalue()
    expected_page = '<title></title>\n'
    assert page == expected_page

def test_selfclosing_element():
    f = StringIO()
    test_close = h.SelfClosingTag()
    test_close.render(f)
    page = f.getvalue()
    expected_page = '<html />\n'
    assert page == expected_page

def test_hr_element():
    f = StringIO()
    test_hr = h.Hr()
    test_hr.render(f)
    page = f.getvalue()
    expected_page = '<hr />\n'
    assert page == expected_page

def test_br_element():
    f = StringIO()
    test_br = h.Br()
    test_br.render(f)
    page = f.getvalue()
    expected_page = '<br />\n'
    assert page == expected_page

def test_a_element():
    f = StringIO()
    test_a = h.A("http://www.google.com", "Google")
    test_a.render(f)
    page = f.getvalue()
    expected_page = '<a href="http://www.google.com">Google</a>\n'
    assert page == expected_page

def test_ul_element():
    f = StringIO()
    test_ul = h.Ul()
    test_ul.render(f)
    page = f.getvalue()
    expected_page = '<ul>\n</ul>\n'
    assert page == expected_page

def test_li_element():
    f = StringIO()
    test_li = h.Li()
    test_li.render(f)
    page = f.getvalue()
    expected_page = '<li>\n</li>\n'
    assert page == expected_page

def test_h_element():
    f = StringIO()
    test_a = h.H(8, "Google")
    test_a.render(f)
    page = f.getvalue()
    expected_page = '<h8>Google</h8>\n'
    assert page == expected_page

def test_meta_element():
    f = StringIO()
    test_meta = h.Meta()
    test_meta.render(f)
    page = f.getvalue()
    expected_page = '<meta />\n'
    assert page == expected_page