#!/usr/bin/env python3
"""
File Name: test_html_render.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/12/2018
Python Version: 3.6.4
"""
from io import StringIO
import html_render as hr
import pytest

i_string = '    '


def test_content_default():
    # default element
    a = hr.Element()
    assert a.content == []


def test_content():
    # element with content
    a = hr.Element('This is a Test')
    assert a.content == ['This is a Test']


def test_append():
    a = hr.Element()
    a.append('This is more content')
    assert 'This is more content' in a.content
    b = hr.Element('Some Content')
    b.append('This is more content')
    assert 'This is more content' in b.content


def test_render():
    a = hr.Element('Some Content.')
    a.append('Some more Content.')
    a.tag = 'html'
    output = StringIO()
    a.render(output)
    assert f'<html>\n    Some Content. Some more Content. \n</html>\n' in output.getvalue()
    output.close()


def test_html():
    a = hr.Html('Some Content.')
    a.append('Some more Content.')
    output = StringIO()
    a.render(output)
    assert f'<html>\n    Some Content. Some more Content. \n</html>\n' in output.getvalue()
    assert '<!DOCTYPE html>\n' in output.getvalue()
    output.close()


def test_body():
    a = hr.Body('Some Content.')
    a.append('Some more Content.')
    output = StringIO()
    a.render(output)
    assert f'<body>\n    Some Content. Some more Content. \n</body>\n' in output.getvalue()
    output.close()


def test_paragraph():
        a = hr.P('Some Content.')
        a.append('Some more Content.')
        output = StringIO()
        a.render(output)
        assert f'<p>\n    Some Content. Some more Content. \n</p>\n' in  output.getvalue()
        output.close()


def test_append_body():
    a = hr.Html()
    b = hr.Body('This is some content')
    a.append(b)
    output = StringIO()
    a.render(output)
    assert b in a.content
    assert issubclass(type(b), hr.Element)
    assert 'This is some content' in output.getvalue()


def test_append_p():
    a = hr.Html()
    b = hr.Body()
    b.append(hr.P('This is some content.'))
    a.append(b)
    output = StringIO()
    a.render(output)
    elements = ('<p>\n', 'This is some content. \n', '</p>\n')
    for element in elements:
        assert element in output.getvalue()


def test_head():
    a = hr.Html()
    b = hr.Head('This is the header')
    a.append(b)
    output = StringIO()
    a.render(output)
    elements = ('<head>\n', 'This is the header \n', '</head>\n')
    for element in elements:
        assert element in output.getvalue()


def test_onelinetag():
    t = hr.OneLineTag('This is a tag')
    t.tag = 'title'
    output = StringIO()
    t.render(output)
    assert '<title>This is a tag</title>\n' in output.getvalue()


def test_title():
    t = hr.Title('This is a title')
    output = StringIO()
    t.render(output)
    assert '<title>This is a title</title>\n' in output.getvalue()


def test_keywords():
    a = (hr.P("Here is a paragraph of text -- there could be more of them, "
              "but this is enough  to show that we can do some text",
         style="text-align: center; font-style: oblique;"))
    output = StringIO()
    a.render(output)
    out_text = output.getvalue()
    assert '<p style="text-align: center; font-style: oblique;">' in out_text
    assert 'but this is enough  to show that we can do some text' in out_text


def test_selfclosingtag():
    a = hr.SelfClosingTag()
    a.tag = 'br'
    output = StringIO()
    a.render(output)
    assert "<br />\n" in output.getvalue()
    with pytest.raises(TypeError):
        a = hr.SelfClosingTag('some stuff')


def test_hr():
    a = hr.Hr()
    output = StringIO()
    a.render(output)
    assert "<hr />\n" in output.getvalue()
    with pytest.raises(TypeError):
        a = hr.Hr('some stuff')


def test_br():
    a = hr.Br()
    output = StringIO()
    a.render(output)
    assert "<br />\n" in output.getvalue()
    with pytest.raises(TypeError):
        a = hr.Br('some stuff')


def test_open():
    a = hr.Html("Here is a paragraph of text -- there could be more of them, "
                "but this is enough  to show that we can do some text",
                style="text-align: center; font-style: oblique;")
    output = '    <html style="text-align: center; font-style: oblique;">\n'
    assert output in a.open_tag(indent=1)


def test_a():
    a = hr.A('http://www.google.com', 'link')
    output = StringIO()
    a.render(output)
    assert '<a href="http://www.google.com">link</a>\n' in output.getvalue()


def test_ul():
    a = hr.Ul()
    output = StringIO()
    a.render(output)
    tags = ('<ul>', '</ul>')
    for tag in tags:
        assert tag in output.getvalue()


def test_li():
    a = hr.Li()
    output = StringIO()
    a.render(output)
    tags = ('<li>', '</li>')
    for tag in tags:
        assert tag in output.getvalue()


def test_h():
    a = hr.H(2, "PythonClass - Class 6 example")
    output = StringIO()
    a.render(output)
    assert '<h2>PythonClass - Class 6 example</h2>' in output.getvalue()


def test_meta():
    a = hr.Meta(charset="UTF-8")
    output = StringIO()
    a.render(output)
    assert '<meta charset="UTF-8"/>\n' in output.getvalue()
