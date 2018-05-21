# Test file for html_render.pytest

import pytest
from io import StringIO
from html_render import Element, Html, Body, P, OneLineTag, Title


def test_step1():
    el = Element()
    assert el.tag == 'html'
    assert el.indent == 0
    assert el.content == []

    el.append('hi')
    assert el.content == ['hi']
    el.append('bye')
    assert el.content == ['hi', 'bye']

    f = StringIO()
    el.render(f)
    assert f.getvalue() == ('<html>\n    hi\n    bye\n</html>\n')

    f = StringIO()
    el.render(f, 1)
    assert f.getvalue() == ('    <html>\n        hi\n        bye\n    '
                            '</html>\n')


def test_step2():
    html_el = Html()
    body_el = Body()
    p_el = P()
    assert html_el.tag == 'html'
    assert body_el.tag == 'body'
    assert p_el.tag == 'p'

    html_el.append('hi')
    f = StringIO()
    html_el.render(f)
    assert f.getvalue() == ('<html>\n    hi\n</html>\n')

    page = Html()
    body = Body()
    body.append(P("Some text."))
    body.append(P("More text."))
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = ('<html>\n    <body>\n        <p>\n            Some text.\n'
                '        </p>\n        <p>\n            More text.\n        '
                '</p>\n    </body>\n</html>\n'
                )
    assert f.getvalue() == expected


def test_step3():
    f = StringIO()
    olt = OneLineTag('hi')
    olt.render(f)
    assert f.getvalue() == '<html>hi</html>\n'

    f = StringIO()
    title = Title('hi')
    title.render(f)
    assert f.getvalue() == '<title>hi</title>\n'


def test_step4():
    p = P('hi', style='some_style', style2='other_style')
    assert p.content == ['hi']
    assert p.indent == 0
    assert p.attr == {'style': 'some_style', 'style2': 'other_style'}

    f = StringIO()
    p.render(f)
    assert f.getvalue() == ('<p style="some_style" style2="other_style">\n'
                            '    hi\n</p>\n')
