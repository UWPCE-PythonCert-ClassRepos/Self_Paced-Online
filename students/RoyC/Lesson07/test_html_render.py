#!/usr/bin/env python3

import html_render as hr

from io import StringIO

def test_element():
    # test output with no content
    e = hr.Element()
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html>\n<\html>")
    
    # test output with 1 line of content
    e = hr.Element("test1")
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html>\n    test1\n<\html>")
    
    # test output with 2 lines of content on construct and a current indent
    e = hr.Element()
    e.append("test1")
    e.append("test2")
    f = StringIO()
    e.render(f, "   ")
    assert(f.getvalue() == "   <html>\n       test1\n       test2\n   <\html>")
