"""
Lesson 07 - Testing code for html
"""

import io
import pytest
import unittest

# import all the functions
from html_render import *


def render_result(element, ind=""):
    """
    This function converts what got rendered to a string for ease of checkign
    """
    outfile = io.StringIO()

    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()


class TestingHTML(unittest.TestCase):
    """ Main function for testing render methods"""

    def test_init(self):
        """Test initialization"""
        h = Element()
        h = Element("Starting...")

    def test_append(self):
        """Function to test appending"""
        h = Element("Starting...")
        h.append("Adding...")

    def test_render_element(self):
        """Tests whether the Element can render two pieces of text"""
        h = Element("Starting...")
        h.append("Adding...")

        # This uses the render_results utility above
        file_contents = render_result(h).strip()

        # making sure the content got in there.
        assert("Starting...") in file_contents
        assert("Adding...") in file_contents

        # make sure it's in the right order
        assert file_contents.index("Starting") < file_contents.index("Adding")

        # making sure the opening and closing tags are right.
        assert file_contents.startswith("<html>")
        assert file_contents.endswith("</html>")

    def test_render_element2(self):
        """This function tests whether the Element can render two pieces of text, using different initialization and appending twice """
        h = Element()
        h.append("this is some text")
        h.append("and this is some more text")

        # This uses the render_results utility above
        file_contents = render_result(h).strip()

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
    def test_html(self):
        e = Html("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents
        assert file_contents.endswith("</html>")

    def test_body(self):
        e = Body("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents
        assert file_contents.startswith("<body>")
        assert file_contents.endswith("</body>")

    def test_p(self):
        e = P("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents

        assert file_contents.startswith("<p>")
        assert file_contents.endswith("</p>")

    def test_sub_element(self):
        """
        tests that you can add another element and still render properly
        """
        page = Html()
        page.append("some plain text.")
        page.append(P("A simple paragraph of text"))
        page.append("Some more plain text.")

        file_contents = render_result(page)

        # note: The previous tests should make sure that the tags are getting
        #       properly rendered, so we don't need to test that here.
        assert "some plain text" in file_contents
        assert "A simple paragraph of text" in file_contents
        assert "Some more plain text." in file_contents
        assert "some plain text" in file_contents
        # but make sure the embedded element's tags get rendered!
        assert "<p>" in file_contents
        assert "</p>" in file_contents

    ########
    # Step 3
    ########

    def test_head(self):
        e = Head("This is the Header")

        file_contents = render_result(e).strip()

        assert("This is the Header") in file_contents
        assert file_contents.startswith("<head>")
        assert file_contents.endswith("</head>")

    def test_title(self):
        e = Title("This is the Title")

        file_contents = render_result(e).strip()

        assert("This is the Title") in file_contents
        assert file_contents.startswith("<title>")
        assert file_contents.endswith("</title>")
        assert "\n" not in file_contents

    def test_onelinetag_append(self):
        e = OneLineTag("the initial content")
        e.append("some more content")
        file_contents = render_result(e).strip()

    #####################
    # indentation testing
    #  Uncomment for Step 9 -- adding indentation
    #####################

    def test_indent(self):
        """
        Tests that the indentation gets passed through to the renderer
        """
        html = Html("some content")
        file_contents = render_result(
            html, ind="   ").rstrip()  # remove the end newline

        lines = file_contents.split("\n")
        assert lines[0].startswith("   <")
        assert lines[-1].startswith("   <")

    def test_indent_contents(self):
        """
        The contents in a element should be indented more than the tag
        by the amount in the indent class attribute
        """
        html = Element("some content")
        file_contents = render_result(html, ind="")

        lines = file_contents.split("\n")
        assert lines[1].startswith(Element.indent)

    def test_multiple_indent(self):
        """
        make sure multiple levels get indented fully
        """
        body = Body()
        body.append(P("some text"))
        html = Html(body)

        file_contents = render_result(html)

        lines = file_contents.split("\n")
        for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
            assert lines[i + 1].startswith(i * Element.indent + "<")
        assert lines[4].startswith(3 * Element.indent + "some")

    def test_element_indent1(self):
        """
        Tests whether the Element indents at least simple content
        we are expecting to to look like this:
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
        assert lines[1].startswith(Element.indent + "thi")
        assert lines[2] == "</html>"
        assert file_contents.endswith("</html>")

if __name__ == '__main__':

    # call the main testing function
    unittest.main()
