"""tests the html_render.py file"""

import html_render as hr
from io import StringIO
import unittest


class TestCalc(unittest.TestCase):

    def test_element(self):
        test = hr.Element('test content', keyword='value')
        self.assertEqual(test.content, ['test content'])
        self.assertEqual(test.attributes, {'keyword': 'value'})

    def test_append(self):
        test = hr.Element('Some content.')
        test.append('Some more content.')
        self.assertEqual(test.content, ['Some content.', 'Some more content.'])

    def test_render(self):
        test = hr.Element('Some content.')
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), '<html>Some content.\n</html>')

    def test_OneLineTag(self):
        test = hr.OneLineTag('Some content.')
        test.tag_name = 'title'
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), '<title>Some content.\n</title>')

    def test_SelfClosingTag(self):
        test = hr.SelfClosingTag('Some content.')
        test.tag_name = 'hr'
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), '<hr/>')
