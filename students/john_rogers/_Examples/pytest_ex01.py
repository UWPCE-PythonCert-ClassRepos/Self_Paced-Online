#!/usr/bin/env python3
"""
pytest examples
Author: JohnR
Version: 1.0
Last updated: 2/04/2019
Notes:
"""

import pytest
import html_render as hr
from io import StringIO as sio


@pytest.fixture
def data():
    return hr.Element('text foo', style='text-align: center;'
                                        ' font-style: oblique;')


@pytest.fixture
def base():
    return hr.Element('text foo')


def test_element(data):
    assert data.content == ['text foo']
    assert data.indent == ' '
    assert data.tag == ''
    assert data.kwargs == {'style': 'text-align: center;'
                                    ' font-style: oblique;'}


def test_append(data):
    data.append('test append method')
    assert data.content == ['text foo', 'test append method']


def test_render(base):
    base.tag = 'html'
    file_out = sio()
    base.render(file_out)
    assert file_out.getvalue() == '<html>\ntext foo\n</html>\n'


def test_onelinetag():
    one_tag = hr.OneLineTag('text foo')
    one_tag.tag = 'title'
    file_out = sio()
    one_tag.render(file_out)
    assert file_out.getvalue() == '<title>text foo</title>\n'


def test_add_items(base):
    file_out = sio()
    base.add_items(file_out)
    assert file_out.getvalue() == 'text foo\n'