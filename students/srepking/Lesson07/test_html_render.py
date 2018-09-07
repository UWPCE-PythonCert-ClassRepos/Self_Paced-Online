import unittest
import html_render as hr


class TestHTML(unittest.TestCase):

# Test Step 1 - Create a class Element() and render() method in class Element.
# The html code is output to "test_html_output1.html". Read in the page data
# and test.
    def test_append(self):
        expected_text = "Here is a paragraph of text -- there could be more of them, " \
                      "but this is enough  to show that we can do some text. " \
                      "And here is another piece of text -- you should be able to " \
                      "add any number"

        page = hr.Element()

        page.append("Here is a paragraph of text -- there could be more of them, "
                    "but this is enough  to show that we can do some text")

        page.append("And here is another piece of text -- you should be able to add any number")

        self.assertEqual(page.append(), expected_text)

if __name__ == '__main__':
    unittest.main()