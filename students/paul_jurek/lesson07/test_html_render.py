"""test suite for html render exercise"""

import pytest

import html_render as hr
import run_html_render as run_hr

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
    assert element._start_tag == '<html>'
    assert element._end_tag == '</html>'

def test_body_element_has_body_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.Body()
    assert element.tag == 'body'
    assert element._start_tag == '<body>'
    assert element._end_tag == '</body>'

def test_p_element_has_p_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.P()
    assert element.tag == 'p'
    assert element._start_tag == '<p>'
    assert element._end_tag == '</p>'


@pytest.fixture
def step2_sample_output():
    with open(r'sample_outputs/test_html_output2.html') as f:
        s = f.read()
    return s

def test_step2_output(step2_sample_output):
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text"))

    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    run_hr.render_page(page, "test_html_output2.html")

    with open('test_html_output2.html') as f:
        generated_file = f.read()
    
    assert generated_file == step2_sample_output

