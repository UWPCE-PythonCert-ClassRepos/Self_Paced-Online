#!/usr/bin/env python3

from html_render import Element
from io import StringIO


def test_append():
    html = Element()
    html.append('This is a test.')
    assert html.content == ['This is a test.']


def test_render():
    html = Element()
    html.append('Some words.')
    f = StringIO()
    html.render(f)
    assert f.getvalue() == '<html>\nSome words.\n</html>'
