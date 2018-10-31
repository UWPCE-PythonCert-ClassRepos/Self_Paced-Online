#!/usr/bin/env python3

import io
import pytest
import html_render as hr


def render_result(element, cur_ind=''):
    file_out = io.StringIO()
    element.render(file_out, cur_ind)
    return file_out.getvalue()


def test_init():
    e = hr.Element()
    e = hr.Element("original text")


def test_append():
    e = hr.Element("element to append to")
    e.append("text to append")
    file_contents = render_result(e).strip()
    print(file_contents)

    assert "element to append to" in file_contents
    assert "text to append" in file_contents
    assert file_contents.index("element to") < file_contents.index("text to")
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


def test_render_element2():
    e = hr.Element()
    e.append("append to empty e4 Element")
    e.append("append again to e4")

    file_contents = render_result(e).strip()


def test_html():
    e = hr.Html("text for html tag")


def test_body():
    e = hr.Body("text for body tag")


def test_p():
    e = hr.P("text for paragraph tag")


def test_html():
    e = hr.Html("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e).strip()
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    e = hr.Body("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = hr.P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element_paragraph():
    page = hr.Html()
    page.append("some plain text.")
    page.append(hr.P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents


def test_sub_element_head():
    page = hr.Html()
    page.append("some plain text.")
    page.append(hr.Head("A HEAD paragraph of text"))
    page.append(hr.Body(" Body text."))

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A HEAD paragraph of text" in file_contents
    assert "Body text." in file_contents
    assert file_contents.index("HEAD paragraph") < file_contents.index("Body text.")


def test_sub_element_title():
    page = hr.Html()
    page.append("some plain text.")
    header = hr.Head("A HEAD paragraph of text")
    page.append(header)
    header.append(hr.Title("A Title paragraph of text"))
    page.append(hr.Body(" Body text."))

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A HEAD paragraph of text" in file_contents
    assert "A Title paragraph" in file_contents
    assert file_contents.index("HEAD paragraph") < file_contents.index("A Title paragraph")


def test_title():
    e = hr.Title("This is a Title")

    file_contents = render_result(e).strip()

    assert "This is a Title" in file_contents
    print(file_contents)
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")
    assert "\n" not in file_contents


def test_one_line_tag_append():
    e = hr.OneLineTag("the initial content")
    with pytest.raises(NotImplementedError):
        e.append("some more content")

    file_contents = render_result(e).strip()
    print(file_contents)


def test_attributes():
    e = hr.P("A paragraph of text", style="text-align: center", id="intro")

    file_contents = render_result(e).strip()
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    #       so using only a "P" tag is fine
    assert "A paragraph of text" in file_contents
    # but make sure the embedded element's tags get rendered!
    # first test the end tag is there -- same as always:
    assert file_contents.endswith("</p>")

    # but now the opening tag is far more complex
    # but it starts the same:
    assert file_contents.startswith("<p")
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents


def test_attributes():
    e = hr.P("A paragraph of text", style="text-align: center", id="intro")

    file_contents = render_result(e).strip()
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    #       so using only a "P" tag is fine
    assert "A paragraph of text" in file_contents
    # but make sure the embedded element's tags get rendered!
    # first test the end tag is there -- same as always:
    assert file_contents.endswith("</p>")

    # but now the opening tag is far more complex
    # but it starts the same:
    assert file_contents.startswith("<p ")  # make sure there's space after the p

    # order of the tags is not important in html, so we need to
    # make sure not to test for that
    # but each attribute should be there:
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents

    # # just to be sure -- there should be a closing bracket to the opening tag
    assert file_contents[:-1].index(">") > file_contents.index('id="intro"')
    assert file_contents[:file_contents.index(">")].count(" ") == 3


def test_hr():
    """a simple horizontal rule with no attributes"""
    hr1 = hr.Hr()
    file_contents = render_result(hr1).strip()
    print(file_contents)
    assert file_contents == '<hr/>'


def test_hr_attr():
    """a horizontal rule with an attribute"""
    hr1 = hr.Hr(width=400)
    file_contents = render_result(hr1).strip()
    print(file_contents)
    assert file_contents == '<hr width="400"/>'


def test_content_in_br():
    with pytest.raises(TypeError):
        br = hr.Br("some content")


def test_br():
    br = hr.Br()
    file_contents = render_result(br).strip()
    print(file_contents)
    assert file_contents == "<br/>"


def test_append_content_in_br():
    with pytest.raises(TypeError):
        br = hr.Br()
        br.append("some content")


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = hr.Html("some content")
    file_contents = render_result(html, cur_ind='    ').rstrip()  # remove the end newline

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith("    <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("    <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = hr.Element("some content")
    file_contents = render_result(html, cur_ind='    ')

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(hr.Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = hr.Body()
    body.append(hr.P("some text"))
    html = hr.Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * hr.Element.indent + "<")

    assert lines[4].startswith(3 * hr.Element.indent + "some")


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    <\html>

    More complex indentation should be tested later.
    """
    e = hr.Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert "this is some text" in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    print(lines)
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(2*hr.Element.indent + "thi")
#    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")
