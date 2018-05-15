#!/usr/bin/env python
"""
Test file used to develop (TDD) and test 'html_render.py'
"""

import html_render as hr
from io import StringIO

def test_elem_attributes():
    assert hr.Element.tag_name == 'html'
    assert hr.Element.indentation == '    '

def elem_content():
    e = hr.Element()
    assert e.content == None

def test_append():
    e = hr.Element()
    e.append('test')
    assert e.content == ['test']

def test_render():
    e = hr.Element()
    e.append('test')
    f = StringIO()
    assert e.render(f, 0) == 7



# py.test --cov  -- this will test everything... how to test one file?
