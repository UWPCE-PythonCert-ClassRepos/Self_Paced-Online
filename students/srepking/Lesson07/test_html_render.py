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
        test_text = "<html>\n" \
                    "Some content.\n" \
                    "Some more content.\n" \
                    "</html>\n"

        page = hr.Html()
        page.append("Some content.")
        page.append("Some more content.")
        #And the render will wrap these two pieces of text with html tags, and output to this file.

        f = StringIO()
        page.render(f)
        self.assertEqual(f.getvalue(), test_text)

    def test_render_2(self):
        # Same as test above, but checking that we can pass text through the Element() method:
        test_text = "<html>\n" \
                    "Start with....\n" \
                    "Some content.\n" \
                    "Some more content.\n" \
                    "</html>\n"

        page = hr.Html("Start with....")
        page.append("Some content.")
        page.append("Some more content.")
        #And the render will wrap these two pieces of text with html tags, and output to this file.

        f = StringIO()
        page.render(f)
        self.assertEqual(f.getvalue(), test_text)

#
# Step 2 Testing
#
    # # tests for the new tags
    def test_html(self):
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


if __name__ == '__main__':
    unittest.main()