import unittest
import html_render as hr
from io import StringIO
import pytest


def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()




class TestHTML(unittest.TestCase):

# Test Step 1 - Create a class Element() and render() method in class Element.
# The html code is output to "test_html_output1.html". Read in the page data
# and test.
# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.


    def test_append(self):
        expected_list = ['Here is a paragraph of text.', 'Here is some more.']

        page = hr.Html()

        page.append("Here is a paragraph of text.")

        page.append("Here is some more.")

        self.assertEqual(page.contents, expected_list)

    def test_render_1(self):
        #The render function will take in a filename and indent,
        # and write html formatted content to the file that looks
        # like this:

        page = hr.Html()
        page.append("Some content.")
        page.append("Some more content.")
        #And the render will wrap these two pieces of text with html tags, and output to this file.

        file_contents = render_result(page).strip()
        assert ("<html>") in file_contents
        assert("Some content.") in file_contents
        assert("Some more content.") in file_contents
        print(file_contents)
        assert file_contents.endswith("</html>")

    def test_render_2(self):
        # Same as test above, but checking that we can pass text through the Element() method:

        page = hr.Html("Start with....")
        page.append("Some content.")
        #And the render will wrap these two pieces of text with html tags, and output to this file.

        file_contents = render_result(page).strip()
        assert ("<html>") in file_contents
        assert("Start with....") in file_contents
        assert("Some content.") in file_contents
        print(file_contents)
        assert file_contents.endswith("</html>")

#
# Step 2 Testing
#
    # # tests for the new tags
    def test_html_1(self):
        e = hr.Html("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents
        print(file_contents)
        assert file_contents.endswith("</html>")



    def test_body(self):
        e = hr.Body("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents

        assert file_contents.startswith("<body")
        assert file_contents.endswith("</body>")


    def test_p(self):
        e = hr.P("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents

        assert file_contents.startswith("<p")
        assert file_contents.endswith("</p>")

    def test_sub_element(self):
        """
        tests that you can add another element and still render properly
        """
        page = hr.Html()
        page.append("some plain text.")
        page.append(hr.P("A simple paragraph of text"))
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
        assert "<p" in file_contents
        assert "</p>" in file_contents

#################
# Step 3 Testing #
#################

    def test_Head(self):
        e = hr.Head("this is header")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert "this is header" in file_contents
        assert "and this is some more text" in file_contents
        print(file_contents)
        assert file_contents.startswith("<head")
        assert file_contents.endswith("</head>")

    def test_OneLineTag(self):
        """Tests that OneLineTag writes one line"""
        e = hr.OneLineTag("This Only Takes One Line")

        file_contents = render_result(e).strip()

        assert "This Only Takes One Line" in file_contents
        print(file_contents)

    def test_Title(self):
        """Test that Title renders one line encapsulated with html title."""
        e = hr.Title("This is a Title")
        file_contents = render_result(e).strip()

        assert "This is a Title" in file_contents
        print(file_contents)
        assert file_contents.startswith("<title>")
        assert file_contents.endswith("</title>")

    def test_sub_element_2(self):
        """
        Test that you can add another element and still render properly
        """

        page = hr.Html()
        page.append(hr.Title('Some HTML Page'))
        page.append(hr.Body('This is my body'))
        page.append("some plain text.")
        page.append(hr.P("A simple paragraph of text"))
        page.append("Some more plain text.")

        file_contents = render_result(page)
        print(file_contents) # so we can see it if the test fails

        assert "Some HTML Page" in file_contents
        assert "This is my body" in file_contents
        assert "some plain text" in file_contents
        assert "A simple paragraph of text" in file_contents
        assert "Some more plain text." in file_contents
     # but make sure the embedded element's tags get rendered!
        assert "<p" in file_contents
        assert "</p>" in file_contents
        assert '<title' in file_contents
        assert '<html' in file_contents
        assert '<body' in file_contents

###########
#  Step 4 #
###########
    def test_Element_attributes(self):
        """Test that the new attributes are accessible from the subclasses"""

        page = hr.Html(id='', style='')
        body = hr.Body(id='', style='')
        paragraph = hr.P(id='', style='')
        title = hr.Title(id='', style='')

        self.assertEqual(page.html_format['id'], "")
        self.assertEqual(page.html_format['style'], "")
        self.assertEqual(body.html_format['id'], "")
        self.assertEqual(body.html_format['style'], "")
        self.assertEqual(paragraph.html_format['id'], "")
        self.assertEqual(paragraph.html_format['style'], "")
        self.assertEqual(title.html_format['id'], "")
        self.assertEqual(title.html_format['style'], "")



    def test_Element_attributes1(self):
        """Test that we can pass an arbitrary list of formatting keywords to Element"""
        paragraph=hr.P('Some text', id="Format id", style="Format style")
        file_contents = render_result(paragraph).strip()
        print(file_contents)
        assert 'style="Format style"' in file_contents
        assert 'id="Format id"' in file_contents
        assert '<p ' in file_contents

###########
#  Step 5 #
###########


    def test_Br1(self):
        """Verify formatting a passing works in Br"""

        Br=hr.Br(id="Format id", style="Format style")
        file_contents = render_result(Br).strip()
        print(file_contents)
        assert 'style="Format style"' in file_contents
        assert 'id="Format id"' in file_contents
        assert '<br ' in file_contents


    def test_Br2(self):
        """a simple horizontal rule with no attributes"""
        br = hr.Br()
        file_contents = render_result(br)
        print(file_contents)
        assert file_contents == '<br />\n'

    def test_Br3(self):
        br = hr.Br()
        file_contents = render_result(br)
        print(file_contents)
        assert file_contents == "<br />\n"

    def test_content_in_br(self):
        with pytest.raises(TypeError):
           br = hr.Br("some content")

    def test_append_content_in_br(self):
        with pytest.raises(TypeError):
            br = hr.Br()
            br.append("some content")
###########
#  Step 6 #
###########
    def test_A(self):
        """Test that the A class with render <a href="http://google.com">link to google</a>"""

        a_class = hr.A("http://google.com", "link to google")
        file_contents = render_result(a_class)
        print(file_contents)
        test_text = "<a href=\"http://google.com\">link to google</a>\n"
        self.assertEqual(file_contents, test_text)

###########
#  Step 7 #
###########
    def test_ul(self):
        """Test the bulleted list <ul> tag."""
        ul_class = hr.Ul(style="line-height:200%", id="TheList")
        ul_class.append(hr.Li('The first item in a list.'))
        ul_class.append(hr.Li('The second item in a list', style="color:red"))
        file_contents = render_result(ul_class)
        print(file_contents)
        assert '<ul style="line-height:200%" id="TheList">' in file_contents
        assert '</ul>' in file_contents


    def test_Li(self):
        """Test the Li element class."""
        li_class = hr.Li(style='color:red')
        li_class.append('The first item in a list')
        li_class.append('The second item in a list')
        file_contents = render_result(li_class)
        print(file_contents)
        assert '<li' in file_contents
        assert '</li>' in file_contents
        assert 'The first item in a list' in file_contents
        assert 'style=\"color:red\"' in file_contents


    def test_H(self):
        """Test a header class to create this tag:
        <h2>PythonClass - Class 6 example</h2>"""
        h2_class = hr.H(2, "PythonClass - Class 6 example")
        file_contents = render_result(h2_class)
        print(file_contents)
        assert '<h2>PythonClass - Class 6 example</h2>' in file_contents

###########
#  Step 8 #
###########
    def test_html_2(self):
        """Test the updated Html class that adds “<!DOCTYPE html>”
        tag at the head of the page"""
        e = hr.Html("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents
        assert file_contents.startswith("<!DOCTYPE html>")
        assert file_contents.endswith("</html>")
        print(file_contents)


    def test_meta(self):
        """Test the adding of meta tag to the beginning of the head element.
        This looks like: <meta charset="UTF-8" />"""
        meta_class = hr.Meta(charset="UTF-8")
        file_contents = render_result(meta_class).strip()
        assert "<meta charset=\"UTF-8\"/>" in file_contents
        print(file_contents)

#####################
# indentation testing
#  Uncomment for Step 9 -- adding indentation
#####################


    def test_indent(self):
        """
        Tests that the indentation gets passed through to the renderer
        """
        html = hr.Html("some content")
        file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline

        print(file_contents)
        lines = file_contents.split("\n")
        assert lines[0].startswith("   <")
        print(repr(lines[-1]))
        assert lines[-1].startswith("   <")


    def test_indent_contents(self):
        """
        The contents in a element should be indented more than the tag
        by the amount in the indent class attribute
        """
        html = hr.Element("some content")
        file_contents = render_result(html, ind="")

        print(file_contents)
        lines = file_contents.split("\n")
        assert lines[1].startswith(hr.Element.indent)


    def test_multiple_indent(self):
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


    def test_element_indent1(self):
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
        assert("this is some text") in file_contents

        # break into lines to check indentation
        lines = file_contents.split('\n')
        # making sure the opening and closing tags are right.
        assert lines[0] == "<html>"
        # this line should be indented by the amount specified
        # by the class attribute: "indent"
        assert lines[1].startswith(hr.Element.indent + "thi")
        assert lines[2] == "</html>"
        assert file_contents.endswith("</html>")





if __name__ == '__main__':
    unittest.main()