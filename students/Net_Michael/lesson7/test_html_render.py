#!/usr/bin/env python
# coding: utf-8

import pytest
from io import StringIO
import html_render as hr

def test_element():
    out_element = hr.Element("content message")
    assert out_element.content == ["content message"]

def test_append():
    append_element = hr.Element("append message1")
    append_element.append("append message2")
    assert append_element.content == ["append message1", "append message2"]

def test_render():
    render_element = hr.Element("render text")
    render_element.tag = 'html'
    f = StringIO()
    render_element.render(f)
    assert f.getvalue() == "<html>\n" + render_element.indent + "render text\n</html>\n"

def test_OneLineTag():
    out_OneLineTag = hr.OneLineTag("create title")
    out_OneLineTag.tag = 'title'
    f = StringIO()
    out_OneLineTag.render(f)
    assert f.getvalue() == '<title>create title</title>\n'

def test_SelfClosingTag():
    out_SelfClosingTag = hr.SelfClosingTag()
    out_SelfClosingTag.tag = 'meta'
    f = StringIO()
    out_SelfClosingTag.render(f)
    assert f.getvalue() == '<meta />\n'

def test_A():
    out_A = hr.A("http://google.com", "Link")
    f = StringIO()
    out_A.render(f)
    assert f.getvalue() == '<a href="http://google.com">\n  Link\n</a>\n'

def test_H():
    out_H = hr.H(2, "Header2")
    f = StringIO()
    out_H.render(f)
    assert f.getvalue() == '<h2>Header2</h2>\n'
