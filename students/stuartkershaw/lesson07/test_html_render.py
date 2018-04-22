from io import StringIO
from html_render import Element
from html_render import Html
from html_render import Body
from html_render import P


# Step 1 tests


def test_type_Element():
    test_element = Element(content=None)
    assert isinstance(test_element, Element) is True


def test_class_attributes_Element():
    test_element = Element(content=None)
    assert test_element.tag_name == ''
    assert test_element.indentation == 4


def test_instance_attributes_Element():
    test_element = Element(content=None)
    assert test_element.content == []


def test_append_content_Element():
    test_element = Element(content=None)
    test_element.append('New content')
    assert test_element.content[0].text == 'New content'


def test_render_page_Element():
    test_element = Html(content="Some content.")
    test_element.append('Some more content.')

    f = StringIO()
    test_element.render(f, "")

    assert f.getvalue() == '<html>\n'\
        'Some content.\n'\
        'Some more content.\n'\
        '</html>'


# Step 2 tests


def test_type_Body():
    test_element = Body(content=None)
    assert isinstance(test_element, Body) is True
    assert test_element.tag_name == 'body'
    assert test_element.indentation == 4


def test_nesting_Elements():
    page = Html()
    body = Body()
    body.append(P("Here is a paragraph of text."))
    body.append(P("And here is another paragraph of text."))
    page.append(body)

    f = StringIO()
    page.render(f, "")

    assert f.getvalue() == '<html>\n'\
        '    <body>\n'\
        '        <p>\n'\
        'Here is a paragraph of text.\n'\
        '        </p>\n'\
        '        <p>\n'\
        'And here is another paragraph of text.\n'\
        '        </p>\n'\
        '    </body>\n'\
        '</html>'
