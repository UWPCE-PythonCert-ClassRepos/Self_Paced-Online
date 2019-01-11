#!/usr/bin/env python3

import html_render as hr
from io import StringIO

element = hr.Element('some text')

def test_init():
    assert element.content == ['some text']
    assert element.tag_type == 0

def test_str():
    assert element.__str__() == '<html>\n    some text\n<\\html>\n'

def test_append():
    element.append('stuff')
    assert element.content == ['some text', 'stuff']

def test_render():
    f = StringIO()
    element.render(f)
    assert f.getvalue() == '<html>\n    some text\n<\\html>\n' + \
                           '<html>\n    stuff\n<\\html>\n'

def test_tag():
    assert element.tag('line') == '<html>\n    line\n<\\html>\n'
