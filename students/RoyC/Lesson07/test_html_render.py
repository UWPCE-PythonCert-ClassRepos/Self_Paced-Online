#!/usr/bin/env python3

import html_render as hr

from io import StringIO

def test_html():
    """ test Html output with no content """
    h = hr.Html()
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<!DOCTYPE html>\n<html>\n</html>")
    
def test_body():
    """ test Body output with 1 line of content """
    b = hr.Body("test1")
    f = StringIO()
    b.render(f)
    assert(f.getvalue() == "<body>\n    test1\n</body>")

def test_p():    
    """ test P output with 2 lines of content """
    p = hr.P()
    p.append("test1")
    p.append("test2")
    f = StringIO()
    p.render(f, "   ")
    assert(f.getvalue() == "   <p>\n       test1\n       test2\n   </p>")

def test_nested():
    """ test a nested structure of elements """
    p = hr.P("test1")
    b = hr.Body(p)
    h = hr.Html(b)
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<!DOCTYPE html>\n<html>\n    <body>\n        <p>\n            test1\n        </p>\n    </body>\n</html>")
    
def test_head():
    """ test Head element """
    h = hr.Head("test1", **{"arg1" : "arg2"})
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<head arg1=\"arg2\">\n    test1\n</head>")
    
def test_ul():
    """ test Ul element """
    u = hr.Ul("test1", **{"arg1" : "arg2"})
    f = StringIO()
    u.render(f)
    assert(f.getvalue() == "<ul arg1=\"arg2\">\n    test1\n</ul>")

def test_li():
    """ test Li element """
    l = hr.Li("test1", **{"arg1" : "arg2"})
    f = StringIO()
    l.render(f)
    assert(f.getvalue() == "<li arg1=\"arg2\">\n    test1\n</li>")

def test_h():
    """ test H element """
    h = hr.H(1, "test1")
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<h1>test1</h1>")
    
def test_hr():
    """ test Hr element """
    h = hr.Hr("test1", **{"arg1" : "arg2"})
    f = StringIO()
    h.render(f)
    assert(f.getvalue() == "<hr arg1=\"arg2\" />")
        
def test_br():
    """ test Br element """
    b = hr.Br("test1", **{"arg1" : "arg2"})
    f = StringIO()
    b.render(f)
    assert(f.getvalue() == "<br arg1=\"arg2\" />")
    
def test_meta():
    """ test Meta element """
    m = hr.Meta(**{"arg1" : "arg2"})
    f = StringIO()
    m.render(f)
    assert(f.getvalue() == "<meta arg1=\"arg2\" />")