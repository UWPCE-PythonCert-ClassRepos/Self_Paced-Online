#!/usr/bin/env python3

# Lesson_7 Activity 1 rendering HTML unit testing script

import html_render as hr
from io import StringIO

def test_element():
    elementest = hr.Element("testing my code", style="text-align: center; font-style: oblique;")
    assert elementest.content == ["testing my code"]
    assert elementest.indent == " "
    assert elementest.attributes == {'style': 'text-align: center; font-style: oblique;'}
    assert elementest.tag == ""
    
def test_append_element():
    appendtest = hr.Element("testing my code", style="text-align: center; font-style: oblique;")
    appendtest.append("testing the append function")
    assert appendtest.content == ["testing my code", "testing the append function"]


def test_render():
    rendertest = hr.Element("testing my code")
    rendertest.tag = 'html'
    f = StringIO()
    rendertest.render(f)
    assert f.getvalue() == "<html>\ntesting my code\n</html>\n"

def test_one_liner():
    onelinetest = hr.OneLineTag("Terrific Title Test")
    onelinetest.tag = "title"
    f = StringIO()
    onelinetest.render(f)
    assert f.getvalue() == "<title>Terrific Title Test</title>\n"
    

def test_self_closer():
    selfclosertest = hr.SelfClosingTag()
    selfclosertest.tag = 'br'
    f = StringIO()
    selfclosertest.render(f)
    assert f.getvalue() == "<br>\n"


def test_link_tag():
    linktest = hr.A("http://google.com", "Lucky Link Test")
    f = StringIO()
    linktest.render(f)
    assert f.getvalue() == "<a href=\"http://google.com\">Lucky Link Test</a>\n"


def test_header_tag():
    headertest = hr.H(2, "Happy Header Test")
    f = StringIO()
    headertest.render(f)
    assert f.getvalue() == "<h2>Happy Header Test</h2>\n"    
    
    