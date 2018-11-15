# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:02:49 2018

@author: Laura.Fiorentino
"""


import html_render
from io import StringIO


def test_element():
    tag_test = html_render.Element()
    assert tag_test.tag == 'html'
    assert tag_test.indentation == '     '


def test_append():
    tag_test = html_render.Element(content='test1')
    tag_test.append('test2')
    assert tag_test.content == ['test1', 'test2']


def test_render():
    render_test = html_render.Element(content='test1')
    f = StringIO()
    render_test.render(f)
    assert f.getvalue() == '<html>\ntest1\n</html>'
