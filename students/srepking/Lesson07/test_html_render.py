import unittest
import html_render as hr
from io import StringIO

class TestHTML(unittest.TestCase):

# Test Step 1 - Create a class Element() and render() method in class Element.
# The html code is output to "test_html_output1.html". Read in the page data
# and test.
    def test_append(self):
        expected_list = ['Here is a paragraph of text.', 'Here is some more.']

        page = hr.Element()

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
                    "<\html>\n"

        page = hr.Element()
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
                    "<\html>\n"

        page = hr.Element("Start with....")
        page.append("Some content.")
        page.append("Some more content.")
        #And the render will wrap these two pieces of text with html tags, and output to this file.

        f = StringIO()
        page.render(f)
        self.assertEqual(f.getvalue(), test_text)

if __name__ == '__main__':
    unittest.main()