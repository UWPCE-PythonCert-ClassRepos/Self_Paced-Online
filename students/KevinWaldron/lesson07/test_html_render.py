#!/usr/bin/env python3

import html_render as hr

from io import StringIO

def test_element():
    # Test all args
    e = hr.Element("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html t1=\"t2\">\n    Test\n</html>")

    # Test no args
    e = hr.Element()
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html>\n</html>")

    # Test only attributes
    e = hr.Element(**{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html t1=\"t2\">\n</html>")

    # Test only content
    e = hr.Element("Test")
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html>\n    Test\n</html>")

    # Test the append menthod
    e.append(hr.Body("Test"))
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html>\n    Test\n    <body>\n        Test\n    </body>\n</html>")

def test_text_element():
    e = hr.TextElement("Test")
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "Test")
    try:
        e.append("t")
    except TypeError:
        pass
    else:
        aseet(False)

def test_body():
    e = hr.Body("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<body t1=\"t2\">\n    Test\n</body>")

def test_html():
    e = hr.Html("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<!DOCTYPE html>\n<html t1=\"t2\">\n    Test\n</html>")

def test_p():
    e = hr.P("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<p t1=\"t2\">\n    Test\n</p>")

def test_head():
    e = hr.Head("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<head t1=\"t2\">\n    Test\n</head>")


def test_one_line_element():
    e = hr.OneLineTag("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html t1=\"t2\">Test</html>")

def test_title():
    e = hr.Title("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<title t1=\"t2\">Test</title>")

def test_self_closing_element():
    e = hr.SelfClosingTag(**{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<html t1=\"t2\" />")
    try:
        e.append("t")
    except TypeError:
        pass
    else:
        aseet(False)

def test_hr():
    e = hr.Hr(**{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<hr t1=\"t2\" />")

def test_br():
    e = hr.Br(**{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<br t1=\"t2\" />")

def test_a():
    e = hr.A("http://www.google.com", "Test")
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<a href=\"http://www.google.com\">Test</a>")

def test_ul():
    e = hr.Ul("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<ul t1=\"t2\">\n    Test\n</ul>")

def test_li():
    e = hr.Li("Test", **{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<li t1=\"t2\">\n    Test\n</li>")

def test_h():
    e = hr.H(1, "Test")
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<h1>Test</h1>")

def test_meta():
    e = hr.Meta(**{"t1" : "t2"})
    f = StringIO()
    e.render(f)
    assert(f.getvalue() == "<meta t1=\"t2\" />")