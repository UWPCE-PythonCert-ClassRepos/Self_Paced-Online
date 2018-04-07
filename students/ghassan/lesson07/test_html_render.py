#!/usr/bin/env python3

import pytest
from html_render import Element, Html, P, Body, Head, OneLineTag, Title, SefClosingTag, A, Ul, Li, H


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
    with open('file2.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file2.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<html>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</html>\n' == rendered  # noqa: E501


def test_P():
    element = P('data1')
    element.append('data2')
    with open('file3.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file3.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<p>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</p>\n' == rendered  # noqa: E501


def test_Body():
    element = Body('data1')
    element.append('data2')
    with open('file4.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file4.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<body>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</body>\n' == rendered  # noqa: E501


def test_Head():
    element = Head('data1')
    element.append('data2')
    with open('file5.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file5.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<head>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</head>\n' == rendered  # noqa: E501


def test_OneLineTag():
    element = OneLineTag('data1')
    element.append('data2')
    with open('file6.html', 'w') as file6fh:
        element.render(file6fh)
    with open('file6.html', 'r') as file6fh:
        rendered = file6fh.read()
    assert '<> '+element.indent+'data1 '+element.indent+'data2 '+'</>\n' == rendered  # noqa: E501


def test_Title():
    element = Title('data1')
    element.append('data2')
    with open('file7.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file7.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<title> '+element.indent+'data1 '+element.indent+'data2 '+'</title>\n' == rendered  # noqa: E501


def test_Element_kwargs():
    element = Element('data1', style="text-align: center; font-style: oblique;")  # noqa: E501
    element.tag = 'p'
    element.append('data2')
    with open('file8.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file8.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<p style="text-align: center; font-style: oblique;">\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</p>\n' == rendered  # noqa: E501


def test_SelfClosingTag_with_contents():
    with pytest.raises(TypeError):
        element = SefClosingTag('data1', style="text-align: center; font-style: oblique;")  # noqa: E501
        element.append('data2')
        with open('file9.html', 'w') as file1fh:
            element.render(file1fh)


def test_SelfClosingTag_no_contents():
    element = SefClosingTag(style="text-align: center; font-style: oblique;")  # noqa: E501
    with open('file9.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file9.html', 'r') as filefh:
        rendered = filefh.read()
    assert '< style="text-align: center; font-style: oblique;">\n'+'</>\n' == rendered  # noqa: E501


def test_A():
    element = A('http://google.com', 'link to google')
    with open('file10.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file10.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<a href="http://google.com">\n'+element.indent+'link to google\n</a>\n' == rendered  # noqa: E501


def test_Ul():
    element = Ul('data1')
    element.append('data2')
    with open('file11.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file11.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<ul>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</ul>\n' == rendered  # noqa: E501


def test_Li():
    element = Li('data1')
    element.append('data2')
    with open('file12.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file12.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<li>\n'+element.indent+'data1\n'+element.indent+'data2\n'+'</li>\n' == rendered  # noqa: E501


def test_H():
    element = H(2, 'data1')
    with open('file13.html', 'w') as file1fh:
        element.render(file1fh)
    with open('file13.html', 'r') as filefh:
        rendered = filefh.read()
    assert '<h2> '+element.indent+'data1 '+'</h2>\n' == rendered  # noqa: E501
