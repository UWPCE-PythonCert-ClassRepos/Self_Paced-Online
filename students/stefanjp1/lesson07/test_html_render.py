import pytest
from io import StringIO
from html_render import *

def render_page(page, filename, indent=None):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


def test_class_init():
    blank_class = Element()
    assert blank_class.tag_name == ''
    assert blank_class.indent == 0
    
def test_content():
    simple_class = Element(content='anything')
    assert isinstance(simple_class.content[0], TextWrapper)
    
def test_append():
    append_class = Element(content='anything')
    append_class.append('something')
    assert len(append_class.content) == 2
    
def test_render():
    render_class = Element()
    render_class.append('Some words.')
    f = StringIO()
    render_class.render(f)
    assert f.getvalue() == '<>\nSome words.</>\n'
    
def test_Html():
    html_class = Html()
    assert html_class.tag_name == 'html'
    
    
def test_Body():
    body_class = Body()
    assert body_class.tag_name == 'body'

    
def test_P():
    p_class = P()
    assert p_class.tag_name == 'p'
    
def test_Head():
    head_class = Head()
    assert head_class.tag_name == 'head'
    
def test_Title():
    title_class = Title()
    title_class.append('Some words.')
    f = StringIO()
    title_class.render(f)
    assert f.getvalue() == '<title>Some words.</title>\n'
    
def test_kwargs():
    attrs = {'class':'intro'}
    title_class = Title('Some words.', **attrs)
    f = StringIO()
    title_class.render(f)
    assert f.getvalue() == '<title class="intro">Some words.</title>\n'
    
def test_Hr():
    hr_class = Hr()
    f = StringIO()
    hr_class.render(f)
    assert f.getvalue() == '<hr />\n'
    
def test_A():
    a_class = A("http://google.com", "link")
    f = StringIO()
    a_class.render(f)
    assert f.getvalue() == '<a href="http://google.com">link</a>\n'
    

def test_H():
    h_class = H(2, "The text of the header")
    f = StringIO()
    h_class.render(f)
    assert f.getvalue() == '<h2>The text of the header</h2>\n'