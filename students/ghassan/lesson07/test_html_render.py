#!/usr/bin/env python3

from html_render import Element


def test_Element():
    element = Element()
    assert element.content == list()


def test_append_to_content():
    element = Element("data1")
    element.append_to_content("data2")
    assert element.content == ["data1", "data2"]


def test_render():
    element = Element('data1')
    element.append_to_content('data2')
    with open('file1.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file1.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<html>\n'+element.indent+'data1 data2 '+'\n<\html>\n' == rendered

