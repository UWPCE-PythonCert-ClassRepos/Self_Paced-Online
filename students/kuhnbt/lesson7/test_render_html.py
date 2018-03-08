import unittest
import html_render as hr

class HtmlTest(unittest.TestCase):
    def setUp(self):
        self.page = hr.Element()

    def test_append(self):
        self.page.append("Here's a new line")
        self.page.append('And another')
        expected_values = ["Here's a new line", "And another"]
        self.assertEqual(self.page.content, expected_values)

    def test_render(self):
        self.page.content = ['Some content.', 'Some more content.']
        expected_text = "<html>\n    Some content. Some more content.\n"\
                        "</html>"
        self.page.render('',' ')
        self.assertEqual(self.page.text, expected_text)