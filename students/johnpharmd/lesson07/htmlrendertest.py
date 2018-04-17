import unittest
import html_render as hr


class HTMLRenderTest(unittest.TestCase):
    """tests html_render attributes"""

    def setUp(self):
        self.test = hr.Element(content='')

    def test_element(self):
        self.assertEqual(self.test.tag, '')
        self.assertEqual(self.test.indent, 1)
        self.assertEqual(self.test.content, '')

    def test_element_append(self):
        self.test.append('new content')
        self.assertEqual(self.test.content, ' new content')

    def test_element_render(self):
        self.test.content = 'None'
        self.test.tag = 'html'
        self.assertEqual(self.test.render('file.txt', cur_ind=''),
                         ('<html>\n' + self.test.indent * '' +
                          'None\n' + '<\html>').strip('\''))
