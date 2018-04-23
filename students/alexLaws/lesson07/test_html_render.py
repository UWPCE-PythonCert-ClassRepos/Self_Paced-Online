#!/usr/bin/env python3

from html_render import Element
from html_render import style_tags
from html_render import Html
from html_render import Head
from html_render import Body
from html_render import P
from html_render import OneLineTag
from html_render import Title
from html_render import A
from html_render import H
from html_render import SelfClosingTag
from html_render import Hr
from html_render import Br
from html_render import Meta
from html_render import Ul
from html_render import Li
from io import StringIO


def test_content():
    blah = Element(content='blah blah blah')
    assert blah.content == ['blah blah blah']


def test_kwarg():
    blah = Element(style='line-height:200%')
    assert blah.kwargs == {'style': 'line-height:200%'}


def test_append():
    html = Element()
    html.append('This is a test.')
    assert html.content == ['This is a test.']


def test_render():
    html = Element()
    html.append('Some words.')
    f = StringIO()
    html.render(f)
    assert f.getvalue() == '<>\n    Some words.\n</>\n'


def test_style_tags():
    output = style_tags({'style': 'line-height:200%'})
    assert output == ' style=\"line-height:200%\"'


def test_html():
    test = Html(content='an html tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n    an html tag\n</html>\n'


def test_head():
    test = Head(content='a head tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<head>\n    a head tag\n</head>\n'


def test_body():
    test = Body(content='a body tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<body>\n    a body tag\n</body>\n'


def test_p():
    test = P(content='a p tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<p>\n    a p tag\n</p>\n'


def test_oneLineTag():
    test = OneLineTag(content='a one line tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<>a one line tag</>\n'


def test_title():
    test = Title(content='a title tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<title>a title tag</title>\n'


def test_a():
    test = A('espn.com', content='an a tag serving as a link')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<a href="espn.com">an a tag serving as a link</a>\n'


def test_h():
    test = H(2, content='an h2 tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<h2>an h2 tag</h2>\n'


def test_selfClosingTag():
    test = SelfClosingTag()
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '< />\n'


def test_hr():
    test = Hr()
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<hr />\n'


def test_br():
    test = Br()
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<br />\n'


def test_meta():
    test = Meta()
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<meta />\n'


def test_ul():
    test = Ul('an unordered list tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<ul>\n    an unordered list tag\n</ul>\n'


def test_li():
    test = Li('a list item tag')
    f = StringIO()
    test.render(f)
    assert f.getvalue() == '<li>\n    a list item tag\n</li>\n'
