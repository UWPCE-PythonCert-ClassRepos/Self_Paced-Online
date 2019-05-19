import html_render as hr
import pytest
from io import StringIO

def test_element_init():
    element = hr.Element()
    assert(element.contents == [])
    test_string = "test string"
    element = hr.Element(test_string)
    assert(element.contents == [test_string])
    #fail_items = [(), [], {}, set(), 3, False]
    #for item in fail_items:
    #    with pytest.raises(TypeError):
    #        element = hr.Element(item)


def test_element_append():
    init_string = "init string"
    element = hr.Element()
    test_strings = ["test1", 'test2', 'test3']
    for idx, test_string in enumerate(test_strings):
        element.append(test_string)
        assert(element.contents == test_strings[:idx+1])
    #fail_items = [(), [], {}, set(), None, 3]
    #for item in fail_items:
    #    with pytest.raises(TypeError):
    #        element.append(item)


def test_element_render():
    test_string = "test string"
    element = hr.Element(test_string)
    element.append(test_string)
    goal_string = "<html>\n    {0}\n    {0}\n</html>".format(test_string)
    f = StringIO()
    element.render(f)
    assert goal_string == f.getvalue()

def test_element_renders_elements():
    test_string = "test string"
    element = hr.Element(test_string)
    element2 = hr.Element()
    element2.append(element)
    goal_string = "<html>\n    <html>\n        {0}\n    </html>\n</html>".format(test_string)
    f = StringIO()
    element2.render(f)
    assert goal_string == f.getvalue()

def test_OneLineTag_render():
    test_string = "test string"
    element = hr.OneLineTag(test_string)
    element2 = hr.Element()
    element2.append(element)
    goal_string = "<html>\n    <html>{0}</html>\n</html>".format(test_string)
    f = StringIO()
    element2.render(f)
    assert goal_string == f.getvalue()

def test_attributes_render():
    test_string = "test string"
    element = hr.Element(test_string, id="TheList", style="line-height:200%")
    element.append(test_string)
    goal_string = '<html id="TheList" style="line-height:200%">\n    {0}\n    {0}\n</html>'.format(test_string)
    f = StringIO()
    element.render(f)
    assert goal_string == f.getvalue()

def test_self_closing_render():
    element = hr.SelfClosingTag()
    element2 = hr.Element()
    element2.append(element)
    goal_string = "<html>\n    <html />\n</html>"
    f = StringIO()
    element2.render(f)
    assert goal_string == f.getvalue()

def test_self_closing_content_error():
    with pytest.raises(TypeError):
        element = hr.SelfClosingTag('cat')


def test_A_render():
    test_link = "http://google.com"
    test_string = "test string"
    element = hr.A(test_link, test_string)
    goal_string = '<a href="{}">{}</a>'.format(test_link, test_string)
    f = StringIO()
    element.render(f)
    assert goal_string == f.getvalue()

def test_Hr():
    element = hr.Hr()
    assert(element.tag_name == 'hr')

def test_Br():
    element = hr.Br()
    assert(element.tag_name == 'br')

def test_Html():
    element = hr.Html()
    assert(element.tag_name == 'html')

def test_Body():
    element = hr.Body()
    assert(element.tag_name == 'body')

def test_Html():
    element = hr.P()
    assert(element.tag_name == 'p')

def test_Head():
    element = hr.Head()
    assert(element.tag_name == 'head')

def test_Title():
    element = hr.Title()
    assert(element.tag_name == 'title')