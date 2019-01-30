#!/usr/bin/env python3
# unit testing for module html_render.py

import pytest
import html_render as hr


def test_element():
    test01 = hr.Element('text foo', style="text-align: center;"
                                          " font-style: oblique;")
    assert test01.content == ['text foo']
    assert test01.indent == '    '
    assert test01.tag == ''
    assert test01.kwargs == {'style': 'text-align: center;'
                                      ' font-style: oblique;'}


