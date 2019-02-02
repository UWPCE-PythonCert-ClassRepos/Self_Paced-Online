#!/usr/bin/env python3
"""
pytest module for testing html_render
"""

import html_render as hr
from io import StringIO as sio


def test_element():
    test01 = hr.Element('text foo', style="text-align: center;"
                                          " font-style: oblique;")
    assert test01.content == ['text foo']
    assert test01.indent == '    '
    assert test01.tag == ''
    assert test01.kwargs == {'style': 'text-align: center;'
                                      ' font-style: oblique;'}


def test_append():
    test02 = hr.Element('test02')
    test02.append('test append method')
    assert test02.content == ['test02', 'test append method']


def test_render():
    test03 = hr.Element('test03')
    test03.tag = 'html'
    foo = sio()
    test03.render(foo)
    assert foo.getvalue() == '<html>\ntest03\n</html>\n'


def test_onelinetag():
    test04 = hr.OneLineTag('test04')
    test04.tag = 'title'
    foo = sio()
    test04.render(foo)
    assert foo.getvalue() == '<title>test04</title>'


def test_selfclosingtag():
    test05 = hr.SelfClosingTag()