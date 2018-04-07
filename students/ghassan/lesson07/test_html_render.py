#!/usr/bin/env python3

from html_render import Element, Html, P, Body


def test_Element():
    element = Element()
    assert element.content == list()


def test_append():
    element = Element("data1")
    element.append("data2")
    assert element.content == ["data1", "data2"]


def test_render():
    element = Element('data1')
    element.append('data2')
    with open('file1.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file1.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</>\n' == rendered  # noqa: E501


def test_Html():
    element = Html('data1')
    element.append('data2')
    with open('file1.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file1.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<html>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</html>\n' == rendered  # noqa: E501


def test_P():
    element = P('data1')
    element.append('data2')
    with open('file1.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file1.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<p>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</p>\n' == rendered  # noqa: E501


def test_Body():
    element = Body('data1')
    element.append('data2')
    with open('file1.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file1.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<body>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</body>\n' == rendered  # noqa: E501
