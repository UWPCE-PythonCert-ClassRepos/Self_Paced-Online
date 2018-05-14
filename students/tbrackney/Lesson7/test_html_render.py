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
    a = hr.Element('Some Content')
    a.append('Some more Content')
    a.tag = 'html'
    output = StringIO()
    a.render(output)
    assert output.getvalue() == f'<html>\n    Some Content. Some more Content. \n</html>\n'
    output.close()


def test_html():
    a = hr.Html('Some Content')
    a.append('Some more Content')
    output = StringIO()
    a.render(output)
    assert output.getvalue() == f'<html>\n    Some Content. Some more Content. \n</html>\n'
    output.close()


def test_body():
    a = hr.Body('Some Content')
    a.append('Some more Content')
    output = StringIO()
    a.render(output)
    assert output.getvalue() == f'<body>\n    Some Content. Some more Content. \n</body>\n'
    output.close()


def test_paragraph():
        a = hr.P('Some Content')
        a.append('Some more Content')
        output = StringIO()
        a.render(output)
        assert output.getvalue() == f'<p>\n    Some Content. Some more Content. \n</p>\n'
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
    b.append(hr.P('This is some content'))
    a.append(b)
    output = StringIO()
    a.render(output)
    assert f'<p>\n    This is some content. \n</p>\n' in output.getvalue()
