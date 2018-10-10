#!/usr/bin/env python

import html_render as hr
from io import StringIO

def test_element():
    test1 = hr.Element('intro', color = 'blue')
    # test1.append('test text')
    assert ['intro'] == test1.content

def test_onelinetag():
    test2 = hr.OneLineTag('intro2')
    # test2.append('test text2')
    assert ['intro2'] == test2.content

def test_selfclosingtag():
    test3 = hr.SelfClosingTag('intro3')
    # test3.append('test text3')
    assert ['intro3'] == test3.content

def test_render():
    test4 = hr.Element('intro')
    f = StringIO()
    test4.render(f)
    assert f.getvalue() == '<html>\nintro\n</html>\n'

# def test_append_render():
#    test5 = hr.Element('intro')
#    test5.append('test text')
#    f = StringIO
#    test5.render(f)
#    assert f.getvalue() == '<html>\nintro\n</html>\n'