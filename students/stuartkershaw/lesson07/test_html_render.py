import pytest
from io import StringIO

from html_render import Element
from html_render import Html
from html_render import Body
from html_render import P
from html_render import Head
from html_render import Title
from html_render import Hr
from html_render import A
from html_render import H
from html_render import Meta


# Step 1


def test_class_attributes_element():
    test_element = Element()
    assert test_element.tag_name == ''
    assert test_element.indentation == 4


def test_instance_attributes_element():
    test_element = Element()
    assert test_element.content == []


def test_append_content_element():
    test_element = Element()
    test_element.append('New content')
    assert test_element.content[0].text == 'New content'


def test_render_page_element():
    test_element = Html(content="Some content.")
    test_element.append('Some more content.')

    f = StringIO()
    test_element.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        'Some content.'\
        'Some more content.'\
        '</html>'


# Step 2


def test_type_body():
    test_element = Body()
    assert test_element.tag_name == 'body'
    assert test_element.indentation == 4


def test_nesting_elements():
    page = Html()
    body = Body()
    body.append(P("Here is a paragraph of text."))
    body.append(P("And here is another paragraph of text."))
    page.append(body)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <body>\n'\
        '        <p>Here is a paragraph of text.</p>\n'\
        '        <p>And here is another paragraph of text.</p>\n'\
        '    </body>\n'\
        '</html>'


# Step 3


def test_onelinetag():
    page = Html()
    head = Head()
    head.append(Title("Here is some title text"))
    page.append(head)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <head>\n'\
        '        <title>Here is some title text</title>\n'\
        '    </head>\n'\
        '</html>'


# Step 4

def test_element_with_attributes():
    page = Html()
    body = Body()
    attributes = {"class": "paragraph", "id": "intro"}
    body.append(P("Here is some paragraph text.", **attributes))
    page.append(body)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <body>\n'\
        '        <p class="paragraph" id="intro">Here is some paragraph text.</p>\n'\
        '    </body>\n'\
        '</html>'


# Step 5


def test_selfclosingtag():
    page = Html()
    body = Body()
    attributes = {"class": "main bordered", "id": "top-spacer"}
    body.append(Hr(**attributes))
    page.append(body)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <body>\n'\
        '        <hr class="main bordered" id="top-spacer" />\n'\
        '    </body>\n'\
        '</html>'


def test_selfclosingtag_with_content():
    with pytest.raises(TypeError) as excinfo:
        page = Html()
        body = Body()
        attributes = {"class": "main bordered", "id": "top-spacer"}
        body.append(Hr("This should break stuff!", **attributes))
        page.append(body)

        f = StringIO()
        page.render(f, "")

        raise TypeError("This element does not accept nested content.")

    assert str(excinfo.value) == "This element does not accept nested content."


# Step 6

def test_a():
    page = Html()
    body = Body()
    body.append(A("http://google.com", "link"))
    page.append(body)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <body>\n'\
        '<a href="http://google.com">link</a>    </body>\n'\
        '</html>'


# Step 7

def test_h():
    page = Html()
    body = Body()
    body.append(H(1, "Top Heading"))
    page.append(body)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <body>\n'\
        '        <h1>Top Heading</h1>\n'\
        '    </body>\n'\
        '</html>'


# Step 8

def test_doctype_meta():
    page = Html()
    head = Head()
    head.append(Meta(charset="UTF-8"))
    page.append(head)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<!DOCTYPE html>\n<html>\n'\
        '    <head>\n'\
        '        <meta charset="UTF-8" />\n'\
        '    </head>\n'\
        '</html>'
