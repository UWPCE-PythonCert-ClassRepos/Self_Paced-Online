import unittest
import html_render as hr
from io import StringIO

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
        expected_text = "<>\n    Some content.\n    Some more content.\n"\
                        "</>"
        f = StringIO()
        self.page.render(f, 0)
        self.assertEqual(f.getvalue(), expected_text)

    def test_render_title(self):
        self.title = hr.Title('This is a test title')
        f = StringIO()
        self.title.render(f, 0)
        expected_text = '<title>This is a test title</title>'
        self.assertEqual(f.getvalue(), expected_text)
