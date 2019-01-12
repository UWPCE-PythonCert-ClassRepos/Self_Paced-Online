#!/usr/bin/env python3

import html_render as hr
from io import StringIO

element = hr.Element()
element.append('some text')
# body = hr.Body()
# body.append('body text')
# p1 = hr.P('para1')
# body.append(p1)
# body.append(hr.P('para2'))
# element.append(body)

def test_init():
    assert element.content == ['some text']
    assert element.tag_type == 0

def test_str():
    assert element.__str__() == '<html>\n' + element.indent_size*' ' + \
        'some text\n</html>\n'

def test_append():
    element.append('stuff')
    assert element.content == ['some text', 'stuff']

def test_render():
    f = StringIO()
    element.render(f)
    print(element)
    assert f.getvalue() == '<html>\n' + element.indent_size*' ' + \
        'some text\n' + element.indent_size*' ' + 'stuff\n</html>\n'

def test_apply_tag():
    assert element.apply_tag() == [
        '<html>\n',
        element.indent_size*' ' + 'some text\n',
        element.indent_size*' ' + 'stuff\n',
        '</html>\n'
        ]

def test_tag():
    assert element.tag() == '<html>\n' + element.indent_size*' ' + \
        'some text\n' + element.indent_size*' ' + 'stuff\n</html>\n'

def test_opentag():
    assert element.opentag(0) == '<html>\n'
    assert element.opentag(1) == element.indent_size*' ' + '<html>\n'

def test_closetag():
    assert element.closetag(0) == '</html>\n'
    assert element.closetag(1) == element.indent_size*' ' + '</html>\n'

def test_line():
    assert element.line('text line',0) == (1)*element.indent_size * ' ' + \
        'text line\n'
    assert element.line('text line',1) == (2)*element.indent_size * ' ' + \
        'text line\n'
