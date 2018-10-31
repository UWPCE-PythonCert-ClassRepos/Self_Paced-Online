"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes some sense for testing.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()

########
# Step 1
########

def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


########
# Step 2
########


# tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents


#####################
# indentation testing
#####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith("   <")
    assert lines[-2].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element._Indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(1,4):
        assert lines[i].startswith((i-1) * Element._Indent + "<")

    assert lines[4].startswith(3 * Element._Indent + "some")

# this is for testing indenting -- we'll wait 'till we get to that
def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    </html>

    More complex indentation should be tested later.
    """
    e = Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(Element._Indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")


########
# Step 3
########

# Checks to see if the Doctype tag is at the beginning of the page
def test_doctype():
    page = Html()
    page.append("Sample text here")
    file_contents = render_result(page).strip()
    lines = file_contents.split('\n')
    assert lines[0] == "<!DOCTYPE html>"

# Checks to see if the title tag and contents shows up properly
# Checks to see if the style attributes shows up properly
def test_title_and_style():
    page = Html()
    head = Head()
    head.append(Title("This is a title"))
    page.append(head)
    body = Body()
    body.append(P("This is a block of text",
        style="text-align: center; font-style: oblique;"))
    page.append(body)
    file_contents = render_result(page).strip()
    assert("This is a title") in file_contents
    lines = file_contents.split('\n')
    assert lines[3] == "        <title>This is a title</title>"
    assert lines[6] == '        <p style="text-align: center; font-style: oblique;">'

# Checks to see if a link is inserted properly
def test_link():
    page = Html()
    head = Head()
    head.append(Title("Link to Bing"))
    page.append(head)
    body = Body()
    body.append(P("Because It's Not Google"))
    body.append(Hr())
    body.append("And this is a ")
    body.append(A("https://www.bing.com/", "link"))
    body.append("to Bing")
    page.append(body)
    file_contents = render_result(page).strip()
    assert("And this is a ") in file_contents
    assert("to Bing") in file_contents
    lines = file_contents.split('\n')
    assert lines[7] == "            Because It's Not Google"
    assert lines[10] == "        And this is a "
    assert lines[11] == '        <a href="https://www.bing.com/">link</a>'
    assert lines[12] == "        to Bing"


# Checks to see if the Ul/Li are entered properly
# Checks to see if the int for the header is passed in correctly
def test_list_and_header():
    page = Html()
    head = Head()
    head.append(Title("Greek Alphabet"))
    page.append(head)
    body = Body()
    body.append(H(2, "The Greek Alphabet"))
    body.append(P("Here's a list of the first few letters of the Greek Alphabet"))
    body.append(Hr())
    lst = Ul(id="TheList", style="line-height:200%")
    lst.append(Li("Alpha"))
    lst.append(Li("Beta"))
    lst.append(Li("Gamma"))
    lst.append(Li("Delta"))
    lst.append(Li("Epsilon"))
    lst.append(Li("Zeta"))
    body.append(lst)
    page.append(body)
    file_contents = render_result(page).strip()
    lines = file_contents.split('\n')
    assert lines[6] == "        <h2>The Greek Alphabet</h2>"
    assert lines[11] == '        <ul id="TheList" style="line-height:200%">'
    assert lines[15] == "            <li>"
    assert lines[16] == "                Beta"
    assert lines[17] == "            </li>"


# Check to see if the br/hr/meta tags are self closing
def test_self_closing():
    page = Html()
    head = Head()
    head.append(Meta(charset="UTF-8"))
    head.append(Title("Sample title here"))
    page.append(head)
    body = Body()
    body.append(H(3, "Sample header here"))
    body.append(P("Sample text here"))
    body.append(Hr())
    brk1 = Br()
    brk1.append("Eta Theta Iota")
    brk2 = Br()
    brk2.append("Kappa Lambda Mu")
    body.append(brk1)
    body.append(brk2)
    page.append(body)
    file_contents = render_result(page).strip()
    assert("<br>") not in file_contents
    assert("<hr>") not in file_contents
    lines = file_contents.split('\n')
    assert lines[3] == '        <meta charset="UTF-8" />'
    assert lines[11] == "        <hr />"
    assert lines[15] == "        <br />"