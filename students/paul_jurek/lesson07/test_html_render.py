"""test suite for html render exercise"""
from io import StringIO

import pytest

import html_render as hr

from run_html_render import render_page

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
    f = StringIO()
    page.render(file_out=f)
    assert 1 == 1

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

def test_head_element_has_head_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.Head()
    assert element.tag == 'head'

def test_title_element_has_title_tag():
    """tests when html element is called the tage is returned at html"""
    element = hr.Title()
    assert element.tag == 'title'

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

    render_page(page, "test_html_output2.html")

    with open('test_html_output2.html') as f:
        generated_file = f.read()

    assert generated_file == step2_sample_output


@pytest.fixture
def step3_sample_output():
    with open(r'sample_outputs/test_html_output3.html') as f:
        s = f.read()
    return s

def test_step3_output(step3_sample_output):
    """copied and pasted from run_html_render.py, step3.
    Expect this gives same result as test html"""
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                    "but this is enough  to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

    page.append(body)

    render_page(page, "test_html_output3.html")

    with open('test_html_output3.html') as f:
        generated_file = f.read()

    assert generated_file == step3_sample_output

@pytest.fixture
def step4_sample_output():
    with open(r'sample_outputs/test_html_output4.html') as f:
        s = f.read()
    return s

def test_step4_output(step4_sample_output):
    """copied and pasted from run_html_render.py, step4.
    Expect this gives same result as test html"""
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                    "but this is enough  to show that we can do some text",
                style="text-align: center; font-style: oblique;"))

    page.append(body)

    render_page(page, "test_html_output4.html")

    with open('test_html_output4.html') as f:
        generated_file = f.read()

    assert generated_file == step4_sample_output

@pytest.fixture
def step5_sample_output():
    with open(r'sample_outputs/test_html_output5.html') as f:
        s = f.read()
    return s

def test_step5_output(step5_sample_output):
    """copied and pasted from run_html_render.py, step5.
    Expect this gives same result as test html"""
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                    "but this is enough  to show that we can do some text",
                style="text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    page.append(body)

    render_page(page, "test_html_output5.html")

    with open('test_html_output5.html') as f:
        generated_file = f.read()

    assert generated_file == step5_sample_output

def test_self_closing_errors_with_content():
    """when user initiates self closing tag with content
    then value error is raised"""
    with pytest.raises(ValueError):
        hr.Hr(content='test')

@pytest.fixture
def step6_sample_output():
    with open(r'sample_outputs/test_html_output6.html') as f:
        s = f.read()
    return s

def test_step6_output(step6_sample_output):
    """copied and pasted from run_html_render.py, step6.
    Expect this gives same result as test html"""
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                    "but this is enough  to show that we can do some text",
                style="text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    body.append("And this is a ")
    body.append( hr.A("http://google.com", "link") )
    body.append("to google")

    page.append(body)

    render_page(page, "test_html_output6.html")

    with open('test_html_output6.html') as f:
        generated_file = f.read()

    assert generated_file == step6_sample_output

@pytest.fixture
def step7_sample_output():
    with open(r'sample_outputs/test_html_output7.html') as f:
        s = f.read()
    return s

def test_step7_output(step7_sample_output):
    """copied and pasted from run_html_render.py, step7.
    Expect this gives same result as test html"""
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append( hr.H(2, "PythonClass - Class 6 example") )

    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                    "but this is enough  to show that we can do some text",
                style="text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    list = hr.Ul(id="TheList", style="line-height:200%")

    list.append( hr.Li("The first item in a list") )
    list.append( hr.Li("This is the second item", style="color: red") )

    item = hr.Li()
    item.append("And this is a ")
    item.append( hr.A("http://google.com", "link") )
    item.append("to google")

    list.append(item)

    body.append(list)

    page.append(body)

    render_page(page, "test_html_output7.html")

    with open('test_html_output7.html') as f:
        generated_file = f.read()

    assert generated_file == step7_sample_output