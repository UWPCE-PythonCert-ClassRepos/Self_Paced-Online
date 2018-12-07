import html_render as hr
from io import StringIO


# STEP 1 TESTS
"""
# test element.__init__
def test_element_init_no_content():
    page = hr.Element()
    assert page.content == []


def test_element_init_w_empty_content():
    page = hr.Element("")
    assert page.content == []


def test_element_init_w_content():
    page = hr.Element("hello")
    assert page.content == ["hello"]


# test element.append
def test_element_append_to_empty_no_content():
    page = hr.Element()
    page.append("")
    assert page.content == []


def test_element_append_to_empty_w_content():
    page = hr.Element()
    page.append("one")
    assert page.content == ["one"]


def test_element_append_twice_to_empty_w_content():
    page = hr.Element()
    page.append("one")
    page.append("two")
    assert page.content == ["one", "two"]


def test_element_append_to_nonempty_no_content():
    page = hr.Element("one")
    page.append("")
    assert page.content == ["one"]


def test_element_append_to_nonempty_w_content():
    page = hr.Element("one")
    page.append("two")
    assert page.content == ["one", "two"]


def test_element_append_twice_to_nonempty_w_content():
    page = hr.Element("one")
    page.append("two")
    page.append("three")
    assert page.content == ["one", "two", "three"]


# test element.render
def test_element_render_no_content():
    page = hr.Element()
    f = StringIO()
    page.render(f)
    expected = "<html>\n</html>\n"
    assert f.getvalue() == expected


def test_element_render_w_one_line():
    page = hr.Element("one")
    f = StringIO()
    page.render(f)
    expected = "<html>\n   one\n</html>\n"
    assert f.getvalue() == expected


def test_element_render_w_two_lines():
    page = hr.Element("one")
    page.append("two")
    f = StringIO()
    page.render(f)
    expected = "<html>\n   one\n   two\n</html>\n"
    assert f.getvalue() == expected


def test_element_render_w_indent_no_content():
    page = hr.Element()
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n   </html>\n"
    assert f.getvalue() == expected


def test_element_render_w_indent_w_one_line():
    page = hr.Element("one")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n      one\n   </html>\n"
    assert f.getvalue() == expected


def test_element_render_w_indent_w_two_lines():
    page = hr.Element("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n      one\n      two\n   </html>\n"
    assert f.getvalue() == expected
"""


# STEP 2 TESTS
"""
# test html_element.render
def test_html_element_render_w_indent_w_two_lines():
    page = hr.Html("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n      one\n      two\n   </html>\n"
    assert f.getvalue() == expected


# test body_element.render
def test_body_element_render_w_indent_w_two_lines():
    page = hr.Body("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <body>\n      one\n      two\n   </body>\n"
    assert f.getvalue() == expected


# test paragraph_element.render
def test_paragraph_element_render_w_indent_w_two_lines():
    page = hr.P("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <p>\n      one\n      two\n   </p>\n"
    assert f.getvalue() == expected


# test append and render of elements
def test_recursive_render():
    page = hr.Html()
    body = hr.Body()
    p1 = hr.P()
    body.append(p1)
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <body>\n" \
               "      <p>\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected


# test append and render of elements
def test_recursive_render_with_multiple_paragraphs():
    page = hr.Html()
    body = hr.Body()
    p1 = hr.P("Here is a paragraph of text")
    p2 = hr.P()
    p2.append("And here is another piece of text")
    body.append(p1)
    body.append(p2)
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <body>\n" \
               "      <p>\n" \
               "         Here is a paragraph of text\n" \
               "      </p>\n" \
               "      <p>\n" \
               "         And here is another piece of text\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected
"""


# STEP 3 TESTS
# test title.render
def test_title_render_empty_content():
    page = hr.Title()
    f = StringIO()
    page.render(f)
    expected = "<title></title>\n"
    assert f.getvalue() == expected


def test_title_render():
    page = hr.Title("this is a title")
    f = StringIO()
    page.render(f)
    expected = "<title>this is a title</title>\n"
    assert f.getvalue() == expected


def test_title_render_append_to_empty_content():
    page = hr.Title()
    page.append("this is a title")
    f = StringIO()
    page.render(f)
    expected = "<title>this is a title</title>\n"
    assert f.getvalue() == expected


def test_title_render_append_to_nonempty_content():
    page = hr.Title("this is a title")
    page.append("this is a second title")
    f = StringIO()
    page.render(f)
    expected = "<title>this is a title</title>\n"
    assert f.getvalue() == expected


def test_step_3_html_output():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <head>\n" \
               "      <title>PythonClass = Revision 1087:</title>\n" \
               "   </head>\n" \
               "   <body>\n" \
               "      <p>\n"\
               "         Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "      </p>\n" \
               "      <p>\n" \
               "         And here is another piece of text -- you should be able to add any number\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected

