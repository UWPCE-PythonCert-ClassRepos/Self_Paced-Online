import unittest
import html_render as hr


class HTMLRenderTest(unittest.TestCase):
    """tests html_render output"""

    def setUp(self):
        self.test = hr.Element(content='')

    def test_element(self):
        self.assertEqual(self.test.tag, '')
        self.assertEqual(self.test.indent, '')
        self.assertEqual(self.test.content, '')

    def test_element_content(self):
        self.test.content_list.append('new content')
        self.assertEqual(self.test.content_list, ['', 'new content'])

    def test_element_render(self):
        self.test.content = 'None'
        self.test.tag = 'html'
        self.assertEqual(self.test.render(cur_ind='4'),
                         ('<html>\n' + ' ' * int('4') + 'None\n'
                          + '<\html>').strip('\''))
