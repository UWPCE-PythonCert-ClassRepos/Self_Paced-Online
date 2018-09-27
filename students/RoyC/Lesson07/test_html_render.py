#!/usr/bin/env python3

import html_render as hr

from io import StringIO

def test_html():
    """ test Html output with no content """
    h = hr.Html()
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<html>\n<\\html>\n")
    
def test_body():
    """ test Body output with 1 line of content """
    b = hr.Body("test1")
    f = StringIO()
    b.render(f)
    assert(f.getvalue() == "<body>\n    test1\n<\\body>\n")

def test_p():    
    """ test P output with 2 lines of content """
    p = hr.P()
    p.append("test1")
    p.append("test2")
    f = StringIO()
    p.render(f, "   ")
    assert(f.getvalue() == "   <p>\n       test1\n       test2\n   <\\p>\n")

def test_nested():
    """ test a nested structure of elements """
    p = hr.P("test1")
    b = hr.Body(p)
    h = hr.Html(b)
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<html>\n    <body>\n        <p>\n            test1\n        <\\p>\n    <\\body>\n<\\html>\n")