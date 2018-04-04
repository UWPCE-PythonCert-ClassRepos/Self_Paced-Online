#!/usr/bin/env python

"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import unittest
import html_render as hr

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


class ElementTests(unittest.TestCase):
    ########
    # Step 1
    ########

    def test_init(self):
        """
        This only tests that it can be initialized with and without
        some content -- but it's a start
        """
        e = hr.Element()
        # instantiate without passing in args
        self.assertEqual(e.contents, [])
        self.assertFalse(bool(e.attrs))
        # instantiate with content and attrs
        e = hr.Element('teststring', keyword='some style')
        self.assertEqual(e.contents, ['teststring'])
        self.assertEqual(e.attrs, {'keyword': 'some style'})

    def test_append(self):
        """
        This tests that you can append text

        It doesn't test if it works --
        that will be covered by the render test later
        """
        e = hr.Element('this is some text')
        e.append('some more text')
        self.assertEqual(e.contents, ['this is some text', 'some more text'])

    def test_render_element(self):
        """
        Tests whether the Element can render two pieces of text
        So it is also testing that the append method works correctly.

        It is not testing whether indentation or line feeds are correct.
        """
        e = hr.Element("this is some text")
        e.append("and this is some more text")

        # This uses the render_results utility above
        file_contents = render_result(e).strip()

        # making sure the content got in there.
        self.assertIn("this is some text", file_contents)
        self.assertIn("and this is some more text", file_contents)

        # make sure it's in the right order
        self.assertLess(file_contents.index("this is"),
                        file_contents.index("and this"))

        # # making sure the opening and closing tags are right.
        self.assertTrue(file_contents.startswith('<html>'))
        self.assertTrue(file_contents.endswith('</html>'))

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
        self.assertIn("this is some text", file_contents)

        # break into lines to check indentation
        lines = file_contents.split('\n')
        # making sure the opening and closing tags are right.
        self.assertEqual(lines[0], "<html>")
        # this line should be indented by the amount specified
        # by the class attribute: "indent"
        self.assertTrue(lines[1].startswith(e.ind + "thi"))
        self.assertEqual(lines[2], "</html>")
        self.assertTrue(file_contents.endswith("</html>"))

    # ########
    # # Step 2
    # ########

    # tests for the new tags
    def test_html(self):
        e = hr.Html("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        self.assertIn("this is some text", file_contents)
        self.assertIn("and this is some more text", file_contents)
        print(file_contents)
        self.assertTrue(file_contents.endswith("</html>"))

    def test_body(self):
        e = hr.Body("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        self.assertTrue("this is some text", file_contents)
        self.assertTrue("and this is some more text", file_contents)

        self.assertTrue(file_contents.startswith("<body>"))
        self.assertTrue(file_contents.endswith("</body>"))

    def test_p(self):
        e = hr.P("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        self.assertTrue("this is some text", file_contents)
        self.assertTrue("and this is some more text", file_contents)

        self.assertTrue(file_contents.startswith("<p>\n"))
        self.assertTrue(file_contents.endswith("</p>"))

    def test_sub_element(self):
        """
        tests that you can add another element and still render properly
        """
        page = hr.Html()
        page.append("some plain text.")
        page.append(hr.P("A simple paragraph of text"))
        page.append("Some more plain text.")

        file_contents = render_result(page)
        print(file_contents)  # so we can see it if the test fails

        # note: The previous tests should make sure that the tags are getting
        #       properly rendered, so we don't need to test that here.
        self.assertTrue("some plain text", file_contents)
        self.assertTrue("A simple paragraph of text", file_contents)
        self.assertTrue("Some more plain text.", file_contents)
        self.assertTrue("some plain text", file_contents)
        # but make sure the embedded element's tags get rendered!
        self.assertTrue("<p>", file_contents)
        self.assertTrue("</p>", file_contents)

    # #####################
    # # indentation testing
    # #####################

    def test_indent(self):
        """
        Tests that the indentation gets passed through to the renderer
        """
        html = hr.Html("some content")
        file_contents = render_result(html, ind="   ")

        print(file_contents)
        lines = file_contents.split("\n")
        self.assertTrue(lines[0].startswith("   <"))
        self.assertTrue(lines[-2].startswith("   <"))

    def test_indent_contents(self):
        """
        The contents in a element should be indented more than the tag
        by the amount in the indent class attribute
        """
        html = hr.Element("some content")
        file_contents = render_result(html, ind="")

        print(file_contents)
        lines = file_contents.split("\n")
        self.assertTrue(lines[1].startswith(hr.Element.ind))

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
            self.assertTrue(lines[i + 1].startswith(i * hr.Element.ind + "<"))

        self.assertTrue(lines[4].startswith(3 * hr.Element.ind + "some"))

    ########
    # Step 3 on ward.
    ########

    # Add your tests here!

    def test_OneLineTag(self):
        e = hr.Title("some title")
        file_contents = render_result(e).strip()
        self.assertEqual('<title>some title</title>', file_contents)

        e = hr.A('www.google.com', 'link to google')
        file_contents = render_result(e).strip()
        self.assertEqual(r"""<a href="www.google.com">link to google</a>""", file_contents)

        e = hr.H(3, 'some text')
        file_contents = render_result(e).strip()
        self.assertEqual('<h3>some text</h3>', file_contents)
    
    def test_SelfClosingTag(self):
        e = hr.Meta(charset="UTF-8")
        file_contents = render_result(e).strip()
        self.assertEqual(r"""<meta charset="UTF-8" />""", file_contents)


if __name__ == '__main__':
    unittest.main()
