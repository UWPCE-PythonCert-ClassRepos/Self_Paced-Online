import html_render as hr
from io import StringIO


# STEP 1 TESTS
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
    res_string = "<html>\n</html>\n"
    assert f.getvalue() == res_string


def test_element_render_w_one_line():
    page = hr.Element("one")
    f = StringIO()
    page.render(f)
    res_string = "<html>\n   one\n</html>\n"
    assert f.getvalue() == res_string


def test_element_render_w_two_lines():
    page = hr.Element("one")
    page.append("two")
    f = StringIO()
    page.render(f)
    res_string = "<html>\n   one\n   two\n</html>\n"
    assert f.getvalue() == res_string


def test_element_render_w_indent_no_content():
    page = hr.Element()
    f = StringIO()
    page.render(f, "   ")
    res_string = "   <html>\n   </html>\n"
    assert f.getvalue() == res_string


def test_element_render_w_indent_w_one_line():
    page = hr.Element("one")
    f = StringIO()
    page.render(f, "   ")
    res_string = "   <html>\n      one\n   </html>\n"
    assert f.getvalue() == res_string


def test_element_render_w_indent_w_two_lines():
    page = hr.Element("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    res_string = "   <html>\n      one\n      two\n   </html>\n"
    assert f.getvalue() == res_string

