#!/usr/bin/env python3

import html_render as hr
from io import StringIO

element = hr.Element('some text', style="text-align: center; font-style: oblique;")
olt = hr.OneLineTag('title', style="text-align: center; font-style: oblique;")

print(element.attrs)
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
    assert element.__str__() == element.tag()

def test_append():
    element.append('stuff')
    assert element.content == ['some text', 'stuff']

def test_render():
    f = StringIO()
    element.render(f)
    print(element)
    assert f.getvalue() == element.tag()

def test_apply_tag():
    assert element.apply_tag() == [
        element.opentag(0),
        element.line('some text',0),
        element.line('stuff',0),
        element.closetag(0)
        ]

def test_tag():
    assert element.tag() == ''.join(element.apply_tag())

def test_opentag():
    assert element.opentag(0) == '<html ' + element.stattr() + '>\n'
    assert element.opentag(1) == element.indent_size*' ' + '<html ' + \
        element.stattr() + '>\n'

def test_closetag():
    assert element.closetag(0) == '</html>\n'
    assert element.closetag(1) == element.indent_size*' ' + '</html>\n'

def test_line():
    assert element.line('text line',0) == (1)*element.indent_size * ' ' + \
        'text line\n'
    assert element.line('text line',1) == (2)*element.indent_size * ' ' + \
        'text line\n'

def test_stattr():
    assert element.stattr() == \
        'style="text-align: center; font-style: oblique;"'

def test_olt_opentag():
    assert olt.opentag(0) == '<html ' + element.stattr() + '>'
    assert olt.opentag(1) == olt.indent_size*' ' + '<html ' + \
        element.stattr() + '>'

def test_olt_closetag():
    assert olt.closetag(0) == '</html>\n'
    assert olt.closetag(1) == '</html>\n'

def test_olt_line():
    assert olt.line('hi there', 0) == 'hi there'
    assert olt.line('hi there', 1) == 'hi there'
