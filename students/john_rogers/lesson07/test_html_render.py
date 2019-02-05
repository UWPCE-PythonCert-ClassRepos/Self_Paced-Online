#!/usr/bin/env python3
"""
pytest module for testing html_render
Author: JohnR
Version: .9
Last updated: 2/04/2019
Notes: TODO: use a fixture to pass static test data
"""

import pytest
import html_render as hr
from io import StringIO as sio


@pytest.fixture
def data():
    return hr.Element('text foo', style='text-align: center;'
                                        ' font-style: oblique;')


def test_element(data):
    assert data.content == ['text foo']
    assert data.indent == ' '
    assert data.tag == ''
    assert data.kwargs == {'style': 'text-align: center;'
                                    ' font-style: oblique;'}


def test_append(data):
    data.append('test append method')
    assert data.content == ['text foo', 'test append method']


def test_render():
    test03 = hr.Element('test03')
    test03.tag = 'html'
    file_out = sio()
    test03.render(file_out)
    assert file_out.getvalue() == '<html>\ntest03\n</html>\n'


def test_onelinetag():
    test04 = hr.OneLineTag('test04')
    test04.tag = 'title'
    file_out = sio()
    test04.render(file_out)
    assert file_out.getvalue() == '<title>test04</title>\n'


def test_add_items():
    test05 = hr.Element('test05')
    file_out = sio()
    test05.add_items(file_out)
    assert file_out.getvalue() == 'test05\n'


def test_add_items_no_line():
    test06 = hr.Element('test06')
    file_out = sio()
    test06.add_items_no_line(file_out)
    assert file_out.getvalue() == 'test06'


def test_add_values(data):
    file_out = sio()
    data.add_values(file_out)
    assert file_out.getvalue() == ' style="text-align: center; font-style: oblique;"'




