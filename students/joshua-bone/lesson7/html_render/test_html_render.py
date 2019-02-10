import io
import html_render as hr
import pytest

def test_element_no_args_has_no_content():
    e = hr.Element()
    assert e.content == []

def test_element_string_arg_has_content():
    e = hr.Element("Test String")
    assert e.content == ["Test String"]

def test_element_list_arg_has_content():
    e = hr.Element(["Test1", "Test2"])
    assert e.content == ["Test1", "Test2"]

def test_element_tuple_arg_has_content():
    e = hr.Element(("Test1", "Test2"))
    assert e.content == ["Test1", "Test2"]

def test_element_kwqargs_has_attributes():
    e = hr.Element(k1="v1", k2="v2")
    assert e.attributes == {"k1":"v1", "k2":"v2"}

def test_element_open_tag():
    e = hr.Element()
    assert e.open_tag() == "<default-tag>"

def test_element_close_tag():
    e = hr.Element()
    assert e.close_tag() == "</default-tag>"

def test_element_open_tag_with_attributes():
    e = hr.Element(k1="v1", k2="v2")
    assert e.open_tag() == "<default-tag k1=\"v1\" k2=\"v2\">"

def test_element_renders_single_content():
    test_content = "Test Content"
    e = hr.Element(test_content)
    expected = ("<default-tag>\n"
                "  Test Content\n"
                "</default-tag>\n")

    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected
    
def test_element_renders_multiple_content():
    test_content = ("Test1", "Test2")
    e = hr.Element(test_content)
    expected = ("<default-tag>\n"
                "  Test1\n"
                "  Test2\n"
                "</default-tag>\n")

    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

def test_element_renders_nested_content():
    e1 = hr.Element("Parent")
    e2 = hr.Element("Child")
    e1.append(e2)
    expected = ("<default-tag>\n"
                "  Parent\n"
                "  <default-tag>\n"
                "    Child\n"
                "  </default-tag>\n"
                "</default-tag>\n")
    with io.StringIO() as output:
        e1.render(output)
        assert output.getvalue() == expected

def test_html():
    e = hr.Html()
    expected = ("<!DOCTYPE html>\n"
                "<html>\n"
                "</html>\n")
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

def test_head():
    e = hr.Head()
    assert e.tag == "head"

def test_body():
    e = hr.Body()
    assert e.tag == "body"

def test_p():
    e = hr.P()
    assert e.tag == "p"

def test_one_line_tag():
    e = hr.OneLineTag("Test Content")
    expected = "<default-tag> Test Content </default-tag>\n"
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

def test_title():
    e = hr.Title("Test Content")
    expected = ("<title> Test Content </title>\n")
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

def test_self_closing_tag():
    e = hr.SelfClosingTag(k1="v1")
    expected = "<default-tag k1=\"v1\">\n"
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

def test_self_closing_tag_append_raises_error():
    e = hr.SelfClosingTag()
    with pytest.raises(TypeError):
        e.append("Test Content")

def test_a():
    e = hr.A("www.some-link.com", "Test Content")
    expected = ("<a href=\"www.some-link.com\">\n"
                "  Test Content\n"
                "</a>\n")
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

def test_h():
    e = hr.H(2, "Test Content")
    expected = "<h2> Test Content </h2>\n"
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected


def test_meta():
    e = hr.Meta("UTF-8")
    expected = "<meta charset=\"UTF-8\">\n"
    with io.StringIO() as output:
        e.render(output)
        assert output.getvalue() == expected

  
